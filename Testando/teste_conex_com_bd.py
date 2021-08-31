import mysql.connector

con = mysql.connector.connect(host='localhost',database='baseforca',user='root',password='')

if con.is_connected():
    db_info = con.get_server_info()
    print(' O banco está conectado, versão',db_info)

    InteracaoTabela = con.cursor()
    InteracaoTabela.execute("select palavra from palavraforca where(id=8);")

    id = InteracaoTabela.fetchone()

    print(id)

#from mysql.connector import baseforca

#use baseforca

#palavra_Sorteada = SELECT palavra FROM palavraforca WHERE(id=random.randint(1,51));

#print(palavra_Sorteada)