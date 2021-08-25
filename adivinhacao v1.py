print('Bem vindo ao jogo de Adivinhação')

import random
num_max = int(input('\nO número será sorteado de 1 a quanto?\n=' ))
numero_secreto = random.randint(1,num_max)


total_rodadas = int(input('\nInforme a quantidade de tentativas que você deseja:\n'))
rodada_atual = 0

while(rodada_atual < total_rodadas):

    rodada_atual = rodada_atual + 1
    
    print(f'\033[95m Rodada {rodada_atual} de {total_rodadas}\033[0m')

    print('O número sorteado está entre 1 a %s' % (num_max))
    chute = int(input('Digite seu chute:\n'))
    
    if(chute > num_max or chute < 1):
        print(f'\033[95m' + 'Você deve digitar um número entre 1 e {num_max}' + '\033[0m')
        rodada_atual = rodada_atual - 1
        continue
    
    if(chute == numero_secreto):
        print('\nVocê acertou, Parabéns!')
        break

    elif(chute > numero_secreto):
        print('\033[1m' + '\nVocê errou, Seu chute foi maior do que o número sorteado' + '\033[0m')

    elif(chute < numero_secreto):
        print('\nVocê errou, Seu chute foi menor do que o número sorteado' + '\033[1m')

    if(rodada_atual == total_rodadas):
        print('\nFim de jogo' + '\033[1m')
