def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    ###Vouu criar no futuro uma (interação com um banco de dados) maneira de criar randomicamente a palavra, por isso o nome da variável é random_nome
    random_nome = 'strogonoff'

    ###Transformei um string em uma lista e guardei isso na variável letras_acertadas
    letras_acertadas = list(random_nome)

    
    ###Essa lista deve passar de [s,t,r,o,g,o,n,o,f,f] para ['_','_','_','_','_','_','_','_','_','_']

    ### vou criar um 
    ###For c(contador pra guardar o índice[]) --- no range de 0 ao total de letras da palavra sorteada
    for c in range(0, len(random_nome)):

        ###a cada loop ele transforma um índice da lista(letras_acertadas) para '_'
        letras_acertadas[c] = '_'

    ###printando a lista transformada em string, o '' vai entrar no lugar da vírgula    
    print(' '.join(letras_acertadas))

    ###variável para contar o total de loops
    numero_tentativas = 0

    ###variável para guardar as letras incorretas e printar elas pro usuário
    erros = ''

    ### iniciando um while de 0 a 9 (10 chances)
    while(numero_tentativas<10):
        ###iterando o numero de tentativas
        numero_tentativas += 1
        ###print da rodada atual
        print(f'{numero_tentativas}ª Tentativa')

        ###input para guardar o chute do usuário[.lower(deixa todas letras minúsculas)][.strip(tira todos whitespaces antes, entre e depois)]
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


            


    print("\nFim do jogo")

if(__name__ == "__main__"):
    jogar()