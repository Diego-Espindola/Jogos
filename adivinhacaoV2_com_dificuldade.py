def jogar():
    print('Bem vindo ao jogo de Adivinhação')

    import random

    total_rodadas = 10

    print("Nivel de difilcudade (1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input('\nDigite qual o nível de dificuldade = ' ))

    if(dificuldade==1):
        print('\033[91m\nVocê escolheu a dificuldade fácil')
        print('Você tem 10 chances, o número sorteado está entre 1 e 100\033[0m')
        num_max = 100
        

    elif(dificuldade==2):
        print('\033[91m\nVocê escolheu a dificuldade média')
        print("\nVocê tem 10 chances, o número sorteado está entre 1 a 200\033[0m")
        num_max = 200
        
    elif(dificuldade==3):
        print('\033[91m\nVocê escolheu a dificuldade difícil')
        print("\nVocê tem 10 chances, o número sorteado está entre 1 a 500\033[0m")
        num_max = 500
        
        
    numero_secreto = random.randint(1,(num_max+1))

    maior_chute = num_max
    menor_chute = 1

    rodada_atual = 0

    while(rodada_atual < total_rodadas):

        rodada_atual = rodada_atual + 1
        
        print(f'\033[95mRodada {rodada_atual} de {total_rodadas}\033[0m')

        print(f'O número sorteado está entre {menor_chute} a {maior_chute}')
        chute = int(input('Digite seu chute:'))


        ##Se o chute for correto 
        if(chute == numero_secreto):
            print(f'\033[36mVocê acertou faltando {total_rodadas-rodada_atual} rodadas, Parabéns!\033[0m')
            break


        ##Se o chute for MAIOR
        elif(chute > numero_secreto):
            print('\033[1m\nVocê errou, Seu chute foi maior do que o número sorteado' + '\033[0m')
            maior_chute = chute


        ##Se o chute for MENOR
        elif(chute < numero_secreto):
            print('\033[1m' + '\nVocê errou, Seu chute foi menor do que o número sorteado' + '\033[0m')
            menor_chute = chute

        ##Se o chute for errado
        else:
            print(f'\033[95m' + 'Você deve digitar um número entre {menor_chute} e {maior_chute}' + '\033[0m')
            rodada_atual = rodada_atual - 1
            continue   


    print('\033[36mFim de jogo\033[0m')
    
if(__name__ == "__main__"):
    jogar()