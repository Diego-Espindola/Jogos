def ImportarPalavra():
    import mysql.connector
    import random

    con = mysql.connector.connect(host='localhost',database='baseforca',user='root',password='')

    if con.is_connected():
        db_info = con.get_server_info()
        print(' O banco está conectado, versão',db_info)

        InteracaoTabela = con.cursor()
        InteracaoTabela.execute("select palavra from palavraforca where(id=15);")

        id = InteracaoTabela.fetchone()

        id = ' '.join(id)

        letras_acertadas = list(id)

        for c in range(0, len(id)):

            letras_acertadas[c] = '_'
        print(' '.join(letras_acertadas))

    #from mysql.connector import baseforca

    #use baseforca

    #palavra_Sorteada = SELECT palavra FROM palavraforca WHERE(id=random.randint(1,51));

    #print(palavra_Sorteada)