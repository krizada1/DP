from opcua import Client,ua 
from timeit import time, timeit
from datetime import datetime
import pyodbc
import telnetlib
import pandas as pd
import cryptography
from opcua.crypto import uacrypto

#DATA KTERE JE TREBA VYPLNIT

#dataframe vsech nazvu hodnot typu integer, ktere chceme cist ze serveru opc a ukladat do SQL
df = pd.DataFrame(columns=["/Channel/GeometricAxis/actProgPos",
                                "/Channel/State/feedRateIpoOvr",                     #doladit_nazev
                                "/Channel/Spindle/speedOvr",
                                "/DriveVsa/Drive/r0035",                         #doladit_nazev                        #doladit_nazev
                                "Timestamp"])


#zadani adresy opc serveru
opcserverstring= "opc.tcp://10.64.4.233:4840"
opcstring= 'ns=2;s='

#SQL 
#SQL string - konfigurace sql serveru
sqlstring="Driver={SQL Server};"+"Server=DESKTOP-LMSTPTV\WINCC;"+"Database=CNC;"+"Trusted_Connection=yes;"

#TELNET (is for checking SQL Server avaliability with short timeout)
telnetstring='localhost' 
sqlport=49978 #port of sql server connection

#TOHLE PROBIHA SAMOVOLNE - neni treba nic vyplnovat


#predpriprava promenne pro buffer (pri uspesnem nacteni hodnot bude +1, pri zapsani do SQL -1)
nezapsano = 0

#pripojeni na OPC Server
#client = Client(opcserverstring,timeout=60)  # if anonymous authentication is enabled
client = Client("opc.tcp://OpcUaClient:12345678@10.64.4.233:4840/",timeout=60) #connect using a user
print(client.application_uri)
client.session_timeout = 60000
client.secure_channel_timeout = 300000
client.connect()
print("OPC Server uspesne pripojen")


#pripojeni na SQL Server
conn = pyodbc.connect(sqlstring,timeout=1)


print("SQL Server uspesne pripojen")
print("\n")

blank=len(df.columns)*[0]

while True:
    try:

        Timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
        #nacteni postupne vsech bool hodnot promnennych definovanych v df_bool z OPC Serveru 
        
        #nacteni postupne vsech int hodnot promnennych definovanych v df z OPC Serveru 
        for i in range(len(df.columns)-1):
            node = client.get_node(opcstring+"%s" %df.columns[i])
            node_value = float(node.get_value())
            blank[i]=node_value
        
        blank[len(df.columns)-1]=Timestamp
        df=df.append(pd.DataFrame([blank],columns=df.columns),ignore_index=True)

        print("Data uspesne nactena z OPC  " + Timestamp)
        nezapsano = nezapsano +1

        df_pro_zapsani=df.iloc[-nezapsano:].to_records(index=False)  #radky dataframe, ktere nebyly zapsany jsou transf. na list
        df_tuple=tuple(u for u in (df_pro_zapsani)) #list je pak premeneny na tuple


        try:

            for i in range(nezapsano): #zapisuji se vsechnz dosud nezapsane radky do SQL
                cursor = conn.cursor()
                pro_zapis = tuple(df_tuple[i-nezapsano]) #vytvoreni vektoru v spravnem tvaru pro zapis
                cursor.execute('''INSERT INTO CNC.dbo.data VALUES
                                (''' + (len(df.columns)-1)*'''?,'''+'''?)
                                ''',pro_zapis) #zapisujou se hodnoty odzadu
                conn.commit()  # poslani to SQL
                #
                cursor = conn.cursor()
                conn.commit()  # poslani to SQL

            print("Data uspesne zapsana do SQL " + Timestamp)
            nezapsano=0
            time.sleep(1)
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
        time.sleep(1)