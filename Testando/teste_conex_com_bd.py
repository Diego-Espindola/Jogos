import mysql.connector

con = mysql.connector.connect(host='localhost',database='Server_Forca',user='root',password='')

while True:
    if con.is_connected():
        db_info = con.get_server_info()
        print(' O banco está conectado, versão',db_info)

#from mysql.connector import baseforca

#use baseforca

#palavra_Sorteada = SELECT palavra FROM palavraforca WHERE(id=random.randint(1,51));

#print(palavra_Sorteada)