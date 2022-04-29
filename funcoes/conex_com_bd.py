def ImportarPalavra():
    import mysql.connector
    import random
    con = mysql.connector.connect(host='localhost',database='projeto_dados',user='root',password='')



    if con.is_connected():

        #db_info = con.get_server_info()
        print('O banco está conectado')#, versão',db_info)

        InteracaoTabela = con.cursor()
        InteracaoTabela.execute(f"select palavra from palavraforca where(id={random.randint(1,51)});")

        id = InteracaoTabela.fetchone()

        id = ''.join(id)
    else:
        print('O banco de dados não está conectado')

    if con.is_connected():    

        InteracaoTabela.close()

        con.close()

    return id


    #from mysql.connector import baseforca

    #use baseforca

    #palavra_Sorteada = SELECT palavra FROM palavraforca WHERE(id=random.randint(1,51));

    #print(palavra_Sorteada)
if(__name__ == "__main__"):
    ImportarPalavra()