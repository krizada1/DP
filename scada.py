from opcua import Client
from timeit import time, timeit
from datetime import datetime
import pyodbc
import telnetlib
import pandas as pd


#DATA KTERE JE TREBA VYPLNIT

#dataframe vsech nazvu hodnot typu integer, ktere chceme cist ze serveru opc a ukladat do SQL
df_int = pd.DataFrame(columns=["/Channel/GeometricAxis/ActProqPos[u1,1]",
                                "/Channel/GeometricAxis/ActProqPos[u1,2]",
                                "/Channel/State/feedRatelpoOvr",                     #doladit_nazev
                                "/Channel/Spindle/speedOvr",
                                "/DriveVsa/Drive/r0035[u1]",                         #doladit_nazev
                                "/DriveVsa/Drive/r0035[u2]",                         #doladit_nazev
                                "Timestamp"])


#zadani adresy opc serveru
opcserverstring= "opc.tcp://localhost:49580"
opcstring= 'ns=2;s='

#SQL 

#cesta k tabulkam sql pro ukladani bool a int promennych
booltablestring='''PLC.dbo.bool''' #tohle neni pouzito - zatim nefunguje
inttablestring='''PLC.dbo.int''' #thle neni pouzito - zatim nefunguje

#SQL string - konfigurace sql serveru
sqlstring="Driver={SQL Server};"+"Server=DESKTOP-LMSTPTV\WINCC;"+"Database=PLC;"+"Trusted_Connection=yes;"

#TELNET (is for checking SQL Server avaliability with short timeout)
telnetstring='localhost' 
sqlport=49978 #port of sql server connection

#TOHLE PROBIHA SAMOVOLNE - neni treba nic vyplnovat


#predpriprava promenne pro buffer (pri uspesnem nacteni hodnot bude +1, pri zapsani do SQL -1)
nezapsano = 0

#pripojeni na OPC Server
client = Client(opcserverstring)  # if anonymous authentication is enabled
# client = Client("opc.tcp://user:12345678@1.1.1.53:4840/") #connect using a user
print(client.application_uri)
client.connect()
print("OPC Server uspesne pripojen")


#pripojeni na SQL Server
conn = pyodbc.connect(sqlstring,timeout=1)


print("SQL Server uspesne pripojen")
print("\n")

blankint=len(df_int.columns)*[0]

while True:
    try:

        Timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
        #nacteni postupne vsech bool hodnot promnennych definovanych v df_bool z OPC Serveru 
        
        #nacteni postupne vsech int hodnot promnennych definovanych v df_int z OPC Serveru 
        for i in range(len(df_int.columns)-1):
            node = client.get_node(opcstring+'%s' %df_int.columns[i])
            node_value = int(node.get_value())
            blankint[i]=node_value
        
        blankint[len(df_int.columns)-1]=Timestamp
        df_int=df_int.append(pd.DataFrame([blankint],columns=df_int.columns),ignore_index=True)

        print("Data uspesne nactena z OPC  " + Timestamp)
        nezapsano = nezapsano +1

        df_int_pro_zapsani=df_int.iloc[-nezapsano:].to_records(index=False)  #radky dataframe, ktere nebyly zapsany jsou transf. na list
        df_int_tuple=tuple(u for u in (df_int_pro_zapsani)) #list je pak premeneny na tuple


        try:

            for i in range(nezapsano): #zapisuji se vsechnz dosud nezapsane radky do SQL
                cursor = conn.cursor()
                pro_zapis_int = tuple(df_int_tuple[i-nezapsano]) #vytvoreni vektoru v spravnem tvaru pro zapis
                cursor.execute('''INSERT INTO PLC.dbo.int VALUES
                                (''' + (len(df_int.columns)-1)*'''?,'''+'''?)
                                ''',pro_zapis_int) #zapisujou se hodnoty odzadu
                conn.commit()  # poslani to SQL
                #
                cursor = conn.cursor()
                conn.commit()  # poslani to SQL

            print("Data uspesne zapsana do SQL " + Timestamp)
            nezapsano=0
            time.sleep(1 )
            print("\n")
        except:
            Timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print("SQL nedostupne  " + Timestamp)
            try:
                telnetlib.Telnet(telnetstring, port=sqlport, timeout=1) #zkousi dostupnost SQL severu (musime zadat spravny port SQL serveru)
                conn = pyodbc.connect(sqlstring, timeout = 1)

            except:
                print("Nepovedlo se obnovit spojeni s SQL  " + Timestamp)
                print("\n")
        time.sleep(4)
    except:
        Timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("OPC nedostupne  " +  Timestamp)
        try:
            client.connect()
            print("Spojeni s OPC obnoveno  " + Timestamp)
            print("\n")
        except:
            print("Nepovedlo se obnovit spojeni s OPC  " + Timestamp)
            print("\n")
        time.sleep(5)