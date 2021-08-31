def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


    random_nome = 'strogonoff'

    nome_secreto = list(random_nome)

    

    letras_acertadas = nome_secreto

    for c in range(0, len(random_nome)):
        letras_acertadas[c] = '_'
        
    print(' '.join(letras_acertadas))


    numero_tentativas = 0
    erros = ''
    while(numero_tentativas<10):

        numero_tentativas = numero_tentativas + 1
        print(f'{numero_tentativas}ª Tentativa')


        tentativa = input('Informe uma letra:').lower().strip()

        ###variável para guardar o índice na hora de guardar uma letra acertada
        index = 0
        ###variavel para contar os acertos, pra caso a pessoa errar fazer um print mostrando que errou e guardar também os erros cometidos
        contagem_acerto = 0
        ###FOR para fazer um loop pela palavra random e verificar se a pessoa acertou alguma das letras
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
                       
        ###If para caso a pessoa acerte a palavra inteira           
        if((letras_acertadas.count('_')) == 0):
            ###O .join() serve pra transformar listas em strings
            print('Você acertou, a palavra era', (''.join(letras_acertadas)) )
            break  
        ###printa a palavra com as letras acertadas
        print(' '.join(letras_acertadas))
        ###se a pessoa já tiver errado alguma vez ele começa a mostrar os erros
        if(erros != ''):
            print(f'Os erros até o momento foram = {erros.upper()}')

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