from mypythontools import pyvueeel
from mypythontools.pyvueeel import expose
import pyodbc
import mypythontools
from opcua import Client, ua
import telnetlib
import pandas as pd
import datetime

opcserverstring= "opc.tcp://localhost:49580"

try:
    client = Client(opcserverstring)  # if anonymous authentication is enabled
    client.connect()
    print("OPC Server uspesne pripojen")

except:
    print("OPC Server nedostupny")

try:
    telnetlib.Telnet('localhost', port=49978, timeout=1)

except:
    print("SQL Server nedostupny")


@expose
def get_plot(promenna1,promenna2, pocet_zaznamu,casovani):
    
    import pandas as pd

    conn = pyodbc.connect(
        "Driver={SQL Server};"  # napojeni na server SQL
        "Server=DESKTOP-LMSTPTV\WINCC;"
        "Database=CNC;"
        "Trusted_Connection=yes;",
        timeout=1,
    )

    query='''SELECT TOP %d %s, %s, %s FROM CNC.dbo.data ORDER BY Timing DESC'''% (pocet_zaznamu, promenna1,promenna2,casovani)
    df_query = pd.read_sql_query(query,conn)
    df = pd.DataFrame(df_query, columns=[promenna1,promenna2,casovani])
    return mypythontools.pyvueeel.to_vue_plotly(df)


@expose
def load_slider(
    promenna1
):
    conn = pyodbc.connect(
        "Driver={SQL Server};"  # napojeni na server SQL
        "Server=DESKTOP-LMSTPTV\WINCC;"
        "Database=CNC;"
        "Trusted_Connection=yes;",
        timeout=1,
    )

    cursor = conn.cursor()
    cursor.execute(
        """SELECT TOP 1 "%s" FROM CNC.dbo.data ORDER BY Timing DESC"""% (promenna1)
    )
    rows = cursor.fetchone()
    conn.close()
    return list(rows)

@expose
def connect_opc():
    try:
        telnetlib.Telnet('localhost', port=49580, timeout=1)
        client = Client(opcserverstring)  # if anonymous authentication is enabled
        client.connect()
        boolean = True

    except:
        boolean = False
        
    return boolean 


# End of file
if __name__ == "__main__":
    pyvueeel.run_gui()
