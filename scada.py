from opcua import Client
from timeit import time
from datetime import datetime
import pyodbc
import telnetlib
import pandas as pd


#vytvoreni dataframe pro SQL
df_int = pd.DataFrame(columns=["D1Speed", "D1Load","D2Speed", "D2Load","D3Speed", "D3Load","D4Speed", "D4Load",
                              "D5Speed", "D5Load","P2Speed", "P2Load","P3Speed", "P3Load","ID_pozice", "cartNumber",
                               "PercentageLoad","unloadingCycleTime", "oven1Temperature1","oven2Temperature4",
                               "oven2Temperature3","oven2Temperature2","oven2Temperature1","Timestamp"])

df_bool = pd.DataFrame(columns=["D1Move","D2Move","D3Move","D4Move","D5Move","P2Move","P3Move",
                                       "oven2PowerOff","oven2Fault","oven2Auto","oven1PowerOff","oven1Fault","oven1Auto",
                                       "coolingZone2PowerOn","coolingZone2Fault","coolingZone2Auto","coolingZone1PowerOn",
                                       "coolingZone1Fault","coolingZone1Auto","cabine2Online","cabine1Online","blasterBridged",
                                       "blasterAuto","blasterAlarm","Timestamp"])


nezapsano = 0

client = Client("opc.tcp://localhost:49580")  # if anonymous authentication is enabled
# client = Client("opc.tcp://user:12345678@1.1.1.53:4840/") #connect using a user
print(client.application_uri)
client.connect()
print("OPC Server uspesne pripojen")


conn = pyodbc.connect("Driver={SQL Server};"  # napojeni na server SQL
                         "Server=DESKTOP-LMSTPTV\WINCC;"
                          "Database=PLC;"
                          "Trusted_Connection=yes;",timeout=1)


print("SQL Server uspesne pripojen")
print("\n")

while True:
    try:


        # zacatek nacteni hodnot promennych typu INT #
        # D1
        D1Speed_node = client.get_node('ns=2;s=Paintshop.D1Speed')
        D1Speed = int(D1Speed_node.get_value())
        D1Load_node = client.get_node('ns=2;s=Paintshop.D1Load')
        D1Load = int(D1Load_node.get_value())

        # D2
        D2Speed_node = client.get_node('ns=2;s=Paintshop.D2Speed')
        D2Speed = int(D2Speed_node.get_value())
        D2Load_node = client.get_node('ns=2;s=Paintshop.D2Load')
        D2Load = int(D2Load_node.get_value())

        # D3
        D3Speed_node = client.get_node('ns=2;s=Paintshop.D3Speed')
        D3Speed = int(D3Speed_node.get_value())
        D3Load_node = client.get_node('ns=2;s=Paintshop.D3Load')
        D3Load = int(D3Load_node.get_value())

        # D4
        D4Speed_node = client.get_node('ns=2;s=Paintshop.D4Speed')
        D4Speed = int(D4Speed_node.get_value())
        D4Load_node = client.get_node('ns=2;s=Paintshop.D4Load')
        D4Load = int(D4Load_node.get_value())

        # D5
        D5Speed_node = client.get_node('ns=2;s=Paintshop.D5Speed')
        D5Speed = int(D5Speed_node.get_value())
        D5Load_node = client.get_node('ns=2;s=Paintshop.D5Load')
        D5Load = int(D5Load_node.get_value())

        # P2
        P2Speed_node = client.get_node('ns=2;s=Paintshop.P2Speed')
        P2Speed = int(P2Speed_node.get_value())
        P2Load_node = client.get_node('ns=2;s=Paintshop.P2Load')
        P2Load = int(P2Load_node.get_value())

        # P3
        P3Speed_node = client.get_node('ns=2;s=Paintshop.P3Speed')
        P3Speed = int(P3Speed_node.get_value())
        P3Load_node = client.get_node('ns=2;s=Paintshop.P3Load')
        P3Load = int(P3Load_node.get_value())

        ID_pozice_node = client.get_node('ns=2;s=Paintshop.ID_pozice')
        ID_pozice = int(ID_pozice_node.get_value())

        cartNumber_node = client.get_node('ns=2;s=Paintshop.cartNumber')
        cartNumber = int(cartNumber_node.get_value())

        PercentageLoad_node = client.get_node('ns=2;s=Paintshop.PercentageLoad')
        PercentageLoad = int(PercentageLoad_node.get_value())

        unloadingCycleTime_node = client.get_node('ns=2;s=Paintshop.unloadingCycleTime')
        unloadingCycleTime = int(unloadingCycleTime_node.get_value())

        oven1Temperature1_node = client.get_node('ns=2;s=Paintshop.oven1Temperature1')
        oven1Temperature1 = int(oven1Temperature1_node.get_value())
        oven2Temperature1_node = client.get_node('ns=2;s=Paintshop.oven2Temperature1')
        oven2Temperature1 = int(oven2Temperature1_node.get_value())
        oven2Temperature2_node = client.get_node('ns=2;s=Paintshop.oven2Temperature2')
        oven2Temperature2 = int(oven2Temperature2_node.get_value())
        oven2Temperature3_node = client.get_node('ns=2;s=Paintshop.oven2Temperature3')
        oven2Temperature3 = int(oven2Temperature3_node.get_value())
        oven2Temperature4_node = client.get_node('ns=2;s=Paintshop.oven2Temperature4')
        oven2Temperature4 = int(oven2Temperature4_node.get_value())

        # konec nacteni hodnot promennych typu INT #

        # zacatek nacteni hodnot promennych typu BOOL #

        #Move
        D1Move_node = client.get_node('ns=2;s=Paintshop.D1Move')
        D1Move = bool(D1Move_node.get_value())
        D2Move_node = client.get_node('ns=2;s=Paintshop.D2Move')
        D2Move = bool(D2Move_node.get_value())
        D3Move_node = client.get_node('ns=2;s=Paintshop.D3Move')
        D3Move = bool(D3Move_node.get_value())
        D4Move_node = client.get_node('ns=2;s=Paintshop.D4Move')
        D4Move = bool(D4Move_node.get_value())
        D5Move_node = client.get_node('ns=2;s=Paintshop.D5Move')
        D5Move = bool(D5Move_node.get_value())
        P2Move_node = client.get_node('ns=2;s=Paintshop.P2Move')
        P2Move = bool(P2Move_node.get_value())
        P3Move_node = client.get_node('ns=2;s=Paintshop.P3Move')
        P3Move = bool(P3Move_node.get_value())

        #oven2
        oven2PowerOff_node = client.get_node('ns=2;s=Paintshop.oven2PowerOff')
        oven2PowerOff = bool(oven2PowerOff_node.get_value())
        oven2Auto_node = client.get_node('ns=2;s=Paintshop.oven2Auto')
        oven2Auto = bool(oven2Auto_node.get_value())
        oven2Fault_node = client.get_node('ns=2;s=Paintshop.oven2Fault')
        oven2Fault = bool(oven2Fault_node.get_value())

        #oven1
        oven1PowerOff_node = client.get_node('ns=2;s=Paintshop.oven1PowerOff')
        oven1PowerOff = bool(oven1PowerOff_node.get_value())
        oven1Auto_node = client.get_node('ns=2;s=Paintshop.oven1Auto')
        oven1Auto = bool(oven1Auto_node.get_value())
        oven1Fault_node = client.get_node('ns=2;s=Paintshop.oven1Fault')
        oven1Fault = bool(oven1Fault_node.get_value())

        #coolingZone2
        coolingZone2PowerOn_node = client.get_node('ns=2;s=Paintshop.coolingZone2PowerOn')
        coolingZone2PowerOn = bool(coolingZone2PowerOn_node.get_value())
        coolingZone2Auto_node = client.get_node('ns=2;s=Paintshop.coolingZone2Auto')
        coolingZone2Auto = bool(coolingZone2Auto_node.get_value())
        coolingZone2Fault_node = client.get_node('ns=2;s=Paintshop.coolingZone2Fault')
        coolingZone2Fault = bool(coolingZone2Fault_node.get_value())

        # coolingZone1
        coolingZone1PowerOn_node = client.get_node('ns=2;s=Paintshop.coolingZone1PowerOn')
        coolingZone1PowerOn = bool(coolingZone1PowerOn_node.get_value())
        coolingZone1Auto_node = client.get_node('ns=2;s=Paintshop.coolingZone1Auto')
        coolingZone1Auto = bool(coolingZone1Auto_node.get_value())
        coolingZone1Fault_node = client.get_node('ns=2;s=Paintshop.coolingZone1Fault')
        coolingZone1Fault = bool(coolingZone1Fault_node.get_value())

        # cabine2
        cabine2Online_node = client.get_node('ns=2;s=Paintshop.cabine2Online')
        cabine2Online = bool(cabine2Online_node.get_value())

        # cabine1
        cabine1Online_node = client.get_node('ns=2;s=Paintshop.cabine1Online')
        cabine1Online = bool(cabine1Online_node.get_value())

        # blaster
        blasterBridged_node = client.get_node('ns=2;s=Paintshop.blasterBridged')
        blasterBridged = bool(blasterBridged_node.get_value())
        blasterAuto_node = client.get_node('ns=2;s=Paintshop.blasterAuto')
        blasterAuto = bool(blasterAuto_node.get_value())
        blasterAlarm_node = client.get_node('ns=2;s=Paintshop.blasterAlarm')
        blasterAlarm = bool(blasterAlarm_node.get_value())

        # konec nacteni hodnot promennych typu BOOL #

        Timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("Data uspesne nactena z OPC  " + Timestamp)  # Vypsani pozadovanych dat
        nezapsano = nezapsano +1


        # vlozeni dat do dataframu

        df_int = df_int.append({"D1Speed":D1Speed,"D1Load":D1Load,"D2Speed":D2Speed,"D2Load":D2Load,"D3Speed":D3Speed,"D3Load":D3Load,"D4Speed":D4Speed,"D4Load":D4Load,
                        "D5Speed":D5Speed,"D5Load":D5Load,"P2Speed":P2Speed,"P2Load":P2Load,"P3Speed":P3Speed,"P3Load":P3Load,"ID_pozice":ID_pozice,"cartNumber":cartNumber,
                        "PercentageLoad":PercentageLoad,"unloadingCycleTime":unloadingCycleTime,"oven1Temperature1":oven1Temperature1,"oven2Temperature4":oven2Temperature4,
                        "oven2Temperature3":oven2Temperature3,"oven2Temperature2":oven2Temperature2,"oven2Temperature1":oven2Temperature1,"Timestamp":Timestamp}, ignore_index=True)

        df_bool = df_bool.append({"D1Move":D1Move,"D2Move":D2Move,"D3Move":D3Move,"D4Move":D4Move,"D5Move":D5Move,"P2Move":P2Move,"P3Move":P3Move,
                                       "oven2PowerOff":oven2PowerOff,"oven2Fault":oven2Fault,"oven2Auto":oven2Auto,"oven1PowerOff":oven1PowerOff,"oven1Fault":oven1Fault,"oven1Auto":oven1Auto,
                                       "coolingZone2PowerOn":coolingZone2PowerOn,"coolingZone2Fault":coolingZone2Fault,"coolingZone2Auto":coolingZone2Auto,"coolingZone1PowerOn":coolingZone1PowerOn,
                                       "coolingZone1Fault":coolingZone1Fault,"coolingZone1Auto":coolingZone1Auto,"cabine2Online":cabine2Online,"cabine1Online":cabine1Online,"blasterBridged":blasterBridged,
                                       "blasterAuto":blasterAuto,"blasterAlarm":blasterAlarm,"Timestamp":Timestamp}, ignore_index=True)

        df_int_pro_zapsani=df_int.iloc[-nezapsano:].to_records(index=False)  #radky dataframe, ktere nebyly zapsany jsou transf. na list
        df_bool_pro_zapsani = df_bool.iloc[-nezapsano:].to_records(index=False) #radky dataframe, ktere nebyly zapsany jsou transf. na list
        df_int_tuple=tuple(u for u in (df_int_pro_zapsani)) #list je pak premeneny na tuple
        df_bool_tuple = tuple(h for h in (df_bool_pro_zapsani)) #list je pak premeneny na tuple

        try:

            for i in range(nezapsano): #zapisuji se vsechnz dosud nezapsane radky do SQL
                cursor = conn.cursor()
                pro_zapis_int = tuple(df_int_tuple[i-nezapsano]) #vytvoreni vektoru v spravnem tvaru pro zapis
                cursor.execute('''INSERT INTO PLC.dbo.int 
                                VALUES
                                (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                                ''',pro_zapis_int) #zapisujou se hodnoty odzadu
                conn.commit()  # poslani to SQL
                #
                cursor = conn.cursor()
                pro_zapis_bool = tuple(df_bool_tuple[i - nezapsano]) #vytvoreni vektoru v spravnem tvaru pro zapis
                cursor.execute('''INSERT INTO PLC.dbo.bool 
                                  VALUES
                                  (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                                    ''',pro_zapis_bool)
                conn.commit()  # poslani to SQL

            print("Data uspesne zapsana do SQL " + Timestamp)
            nezapsano=0
            time.sleep(1 )
            print("\n")
        except:

            print("SQL nedostupne  " + Timestamp)
            try:
                telnetlib.Telnet('localhost', port=49978, timeout=1) #zkousi dostupnost SQL severu
                conn = pyodbc.connect("Driver={SQL Server};"  # napojeni na server SQL
                                      "Server=DESKTOP-LMSTPTV\WINCC;"
                                      "Database=PLC;"
                                      "Trusted_Connection=yes;", timeout = 1)

            except:
                print("Nepovedlo se obnovit spojeni s SQL  " + Timestamp)
                print("\n")
        time.sleep(4)
    except:
        print("OPC nedostupne  " +  Timestamp)
        try:
            client.connect()
            print("Spojeni s OPC obnoveno  " + Timestamp)
            print("\n")
        except:
            print("Nepovedlo se obnovit spojeni s OPC  " + Timestamp)
            print("\n")
        time.sleep(5)

