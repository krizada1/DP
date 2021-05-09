from mypythontools import pyvueeel
from mypythontools.pyvueeel import expose
import pyodbc
import plotly as pl
import mypythontools
from pathlib import Path
from opcua import Client, ua

try:
    client = Client("opc.tcp://localhost:49580")  # if anonymous authentication is enabled
    client.connect()
    print("OPC Server uspesne pripojen")

except:
    print("OPC Server nepripojen")


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
def nacti_z_db(promenna, pocet_zaznamu):
    conn = pyodbc.connect(
        "Driver={SQL Server};"  # napojeni na server SQL
        "Server=DESKTOP-LMSTPTV\WINCC;"
        "Database=PLC;"
        "Trusted_Connection=yes;",
        timeout=1,
    )

    cursor = conn.cursor()
    cursor.execute(
        """SELECT TOP %d %s FROM PLC.dbo.bool ORDER BY Timing DESC"""
        % (pocet_zaznamu, promenna)
    )
    rows = cursor.fetchall()
    rows_as_list = [x for y in rows for x in y]
    for row in rows_as_list:
        print(row)
    conn.close()
    return rows_as_list[0] * 1


@expose
def nacti_switch(
    promenna1,
    promenna2,
    promenna3,
    promenna4,
    promenna5,
    promenna6,
    promenna7,
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
        """SELECT TOP 1 %s,%s,%s,%s,%s,%s,%s,%s FROM PLC.dbo.bool ORDER BY Timing DESC"""
        % ( 
            promenna1,
            promenna2,
            promenna3,
            promenna4,
            promenna5,
            promenna6,
            promenna7,
            scadacontrol,
        )
    )
    rows = cursor.fetchone()
    conn.close()
    return list(rows)


@expose
def nacti_slider(
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
