def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print("Orientações: 1.Você tem 10 chances")
    print("2.Você pode chutar uma letra ou a palavra inteira")
    print("3.Ao final das tentativas você terá uma ultima chance de chutar a palavra inteira")

    ###Vouu criar no futuro uma (interação com um banco de dados) maneira de criar randomicamente a palavra, por isso o nome da variável é random_nome
    random_nome = 'strogonoff'

    ###Transformei um string em uma lista e guardei isso na variável letras_acertadas
    letras_acertadas = list(random_nome)

    ###For para transformar a string em uma lista e muda a letra para '_'
    for c in range(0, len(random_nome)):

        letras_acertadas[c] = '_'
        

    print(' '.join(letras_acertadas))


    numero_tentativas = 0

    erros = ''

    while(numero_tentativas<10):

        numero_tentativas = numero_tentativas + 1

        print(f'{numero_tentativas}ª Tentativa')

        tentativa = input('Informe uma letra:').lower().strip()

        index = 0

        contagem_acerto = 0

        ###If para caso a pessoa escreva a palavra inteira ao invés da letra
        if(tentativa==(random_nome.lower()).strip()):
            
            print('Você acertou, a palavra era', random_nome)

            break  


        ###FOR para fazer um loop pela palavra random guardar se a pessoa acertou ou errou. Será feito um if para caso a pessoa tenha errado guardar todas as letras erradas e mostrar para o usuario
        for letra in random_nome:

            ###IF que verifica se a pessoa acertou alguma letra da palavra random 
            if(tentativa == letra):

                ###Guarda a letra acertada no lugar correto dentro da lista
                letras_acertadas[index] = letra

                ###Troca a variável contagem acerto para 1, fazendo assim com que a (condição) do if seguinte seja false
                contagem_acerto = 1

            index += 1
        
        ###if para caso a pessoa errar guardar o erro e mostrar um print 'voce errou'
        if(contagem_acerto == 0):

            ###guarda os erros cometidos para serem printados 
            erros = erros + ' ' + tentativa

            print('Você errou, tente novamente')
                       
        ###If para caso a pessoa acerte todas as letras          
        if((letras_acertadas.count('_')) == 0):

            ###O .join() serve pra transformar listas em strings
            print('Você acertou, a palavra era', random_nome)

            break  

        ###printa a palavra com as letras acertadas
        print(' '.join(letras_acertadas))

        ###se a pessoa já tiver errado alguma vez ele começa a mostrar os erros
        if(erros != ''):

            print(f'Os erros até o momento foram = {erros.upper()}')

    ###If fora do laço while para caso a palavra ainda não tenha sido acertada
    if((letras_acertadas.count('_')) > 0):

	    print('Você não conseguiu, essa é a sua chance de chutar a palavra')

	    chute_final = (input('Digite seu chute: ').lower()).strip()

	    if(chute_final == random_nome):

	    	print(f'\nParabéns, você acertou, a palavra é {random_nome}')
	    else:

	    	print(f'Você errou, a palavra era {random_nome}')

            


    print("\nFim do jogo")

if(__name__ == "__main__"):
    jogar()