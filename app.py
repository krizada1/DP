from mypythontools import pyvueel
from mypythontools.pyvueel import expose
import pyodbc

# Expose python functions to Js with decorator
@expose
def load_data(neznama):
    # You can return dict - will be object in js
    # You can return list - will be an array in js

    print(666)

    return neznama

    # return {'Hello': 1}

@expose
def nacti_z_db(promenna,pocet_zaznamu):
    conn = pyodbc.connect("Driver={SQL Server};"  # napojeni na server SQL
                         "Server=DESKTOP-LMSTPTV\WINCC;"
                          "Database=PLC;"
                          "Trusted_Connection=yes;",timeout=1)

    
    cursor=conn.cursor()
    cursor.execute('''SELECT TOP %d %s FROM PLC.dbo.bool''' %(pocet_zaznamu,promenna))
    rows=cursor.fetchall()
    rows_as_list = [x for y in rows for x in y]
    for row in rows_as_list:
        print(row)
    conn.close()
    return rows_as_list[0]*1 #array?? graf???


# End of file
if __name__ == '__main__':
    pyvueel.run_gui()
