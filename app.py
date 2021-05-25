from mypythontools import pyvueeel
from mypythontools.pyvueeel import expose
import pyodbc
import mypythontools
from opcua import Client, ua
import telnetlib
import pandas as pd
import datetime

try:
    client = Client("opc.tcp://localhost:49580")  # if anonymous authentication is enabled
    client.connect()
    print("OPC Server uspesne pripojen")

except:
    print("OPC Server nedostupny")

try:
    telnetlib.Telnet('localhost', port=49978, timeout=1)

except:
    print("SQL Server nedostupny")

@expose
def set_switch_value(variable, value):
    variable_node = client.get_node('ns=2;s=Paintshop.%s' %variable) 
    variable_node.set_value(value)
    print("zapsano na opc")

@expose
def set_slider_value(variable, value):
    variable_node = client.get_node('ns=2;s=Paintshop.%s' %variable) 
    datavalue = ua.DataValue(ua.Variant(value, ua.VariantType.Int16))
    variable_node.set_data_value(datavalue)

    #except:
        #try:
            #client = Client("opc.tcp://localhost:49580")  # if anonymous authentication is enabled
            #client.connect()
        #except:
            #print("Nedari se navazat spojeni s OPC - nelze ovladat pres web")

@expose
def get_plot(promenna, pocet_zaznamu,casovani):
    
    import pandas as pd

    conn = pyodbc.connect(
        "Driver={SQL Server};"  # napojeni na server SQL
        "Server=DESKTOP-LMSTPTV\WINCC;"
        "Database=PLC;"
        "Trusted_Connection=yes;",
        timeout=1,
    )

    query='''SELECT TOP %d %s, %s FROM PLC.dbo.int ORDER BY Timing DESC'''% (pocet_zaznamu, promenna,casovani)
    df_query = pd.read_sql_query(query,conn)
    df = pd.DataFrame(df_query, columns=[promenna,casovani])
    return mypythontools.pyvueeel.to_vue_plotly(df)


@expose
def get_table(promenna):

    conn = pyodbc.connect(
        "Driver={SQL Server};"  # napojeni na server SQL
        "Server=DESKTOP-LMSTPTV\WINCC;"
        "Database=PLC;"
        "Trusted_Connection=yes;",
        timeout=1,
    )

      #zdvojnasobi zadany pocet zaznamu, protoze potrebuju zacatek i konec alarmu

    query="""select %s,Timing 
    from (select *,lead(%s) over(order by Timing desc) as prev_value 
    from PLC.dbo.bool 
    ) l where prev_value <> %s""" %(promenna,promenna,promenna)
    
    df_query = pd.read_sql_query(query,conn,parse_dates=["Timing"]) #nacte z SQL, kde "Timing" je datetime
    df = pd.DataFrame(df_query, columns=[promenna,"Timing"]) #vytvoreni df
    
    selected_columns = df[[promenna,"Timing","Timing"]] #zdvojnasobi se sloupce s casem
    new_df = selected_columns.copy()                    #zdvojnasobi se sloupce s casem
    new_df.insert(3, "Duration", int(0), allow_duplicates = True)
    new_df.columns = ['Location', 'Start time', 'Finish time', 'Duration']  #prejmenujou se sloupce
    
    number_of_rows = len(df.index) #zjisti se pocet radku


    for i in range(int(number_of_rows/2)): 
        new_df.at[i*2,'Start time'] = new_df.iloc[2*i+1]['Start time']    #propisuje se hodnota zacatku naspolecny radek jako hodnota konce alarmu
        try:
            new_df.at[i*2,'Duration'] = datetime.timedelta.total_seconds(new_df.iloc[2*i]['Finish time'] - new_df.iloc[2*i]['Start time'])    #propisuje se hodnota zacatku naspolecny radek jako hodnota konce alarmu
        except: 0

    new_df['Location'] = new_df['Location'].replace([True],promenna)
    new_df=new_df.iloc[::2, :] #odstrani se kazdy druhy radek z dataframu
    

    new_df['Start time'] = new_df['Start time'].astype(str)
    new_df['Finish time'] = new_df['Finish time'].astype(str)

    return mypythontools.pyvueeel.to_table(new_df)

@expose
def load_switch(
    promenna1,
    promenna2,
    promenna3,
    promenna4,
    promenna5,
    promenna6,
    promenna7,
):
    conn = pyodbc.connect(
        "Driver={SQL Server};"  # napojeni na server SQL
        "Server=DESKTOP-LMSTPTV\WINCC;"
        "Database=PLC;"
        "Trusted_Connection=yes;",
        timeout=1,
    )

    cursor = conn.cursor()
    cursor.execute(
        """SELECT TOP 1 %s,%s,%s,%s,%s,%s,%s FROM PLC.dbo.bool ORDER BY Timing DESC"""
        % ( 
            promenna1,
            promenna2,
            promenna3,
            promenna4,
            promenna5,
            promenna6,
            promenna7,
        )
    )
    rows = cursor.fetchone()
    conn.close()
    return list(rows)

@expose
def load_scada(
    scadacontrol,
):
    conn = pyodbc.connect(
        "Driver={SQL Server};"  # napojeni na server SQL
        "Server=DESKTOP-LMSTPTV\WINCC;"
        "Database=PLC;"
        "Trusted_Connection=yes;",
        timeout=1,
    )

    cursor = conn.cursor()
    cursor.execute(
        """SELECT TOP 1 %s FROM PLC.dbo.bool ORDER BY Timing DESC"""
        % ( 
            scadacontrol,
        )
    )
    rows = cursor.fetchone()
    conn.close()
    return list(rows)


@expose
def load_slider(
    promenna1,
    promenna2,
    promenna3,
    promenna4,
    promenna5,
    promenna6,
    promenna7,
):
    conn = pyodbc.connect(
        "Driver={SQL Server};"  # napojeni na server SQL
        "Server=DESKTOP-LMSTPTV\WINCC;"
        "Database=PLC;"
        "Trusted_Connection=yes;",
        timeout=1,
    )

    cursor = conn.cursor()
    cursor.execute(
        """SELECT TOP 1 %s,%s,%s,%s,%s,%s,%s FROM PLC.dbo.int ORDER BY Timing DESC"""
        % (
            promenna1,
            promenna2,
            promenna3,
            promenna4,
            promenna5,
            promenna6,
            promenna7,
        )
    )
    rows = cursor.fetchone()
    conn.close()
    return list(rows)


# End of file
if __name__ == "__main__":
    pyvueeel.run_gui()
