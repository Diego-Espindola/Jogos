def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    nome_secreto = 'queijo'
    numero_tentativas = 0

    erros = ''

    while(numero_tentativas<10):

        numero_tentativas = numero_tentativas + 1
        print(f'{numero_tentativas}ª Tentativa')


        tentativa = input('Informe uma letra:').lower().strip()

        if(nome_secreto.count(tentativa.lower())>0):
            for letra in nome_secreto:

                if(tentativa == letra):

                    print(tentativa)
                else:
                    print('|')
        else: 
            erros = erros + ' ' + tentativa
            print('Você errou, tente novamente')
            print(f'Seus chutes até o momento foram:\n{erros}')


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()