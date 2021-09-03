def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    nome_secreto = 'queijo'
    numero_tentativas = 0

    erros = ''

    while(numero_tentativas<10):

        tentativa = input('Informe uma letra:')

        verificacao = nome_secreto.count(tentativa)

        tentativa = tentativa.upper()

        if(verificacao>0):
            print(f"Você acertou, a palavra possui {verificacao} {tentativa.upper()}'s")
        else:
            erros = erros + ' ' + tentativa
            print('Você errou, tente novamente')
            print(f'Seus chutes até o momento foram:\n{erros}')

    



    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()