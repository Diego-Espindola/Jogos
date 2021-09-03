import numpy as np
print('Criando manualmente')
a = np.array([0, 1, 2, 3])
print('1º array\n', a)

b = np.array([[0, 1, 2], [3, 4, 5], [5, 6, 7], [8,9,10]])

#possui duas linhas, cada lista interna é uma linha, e cada item é uma coluna 4x3

print('array com lista bidimensional\n', b)


#como saber a dimensão do array
print(b.ndim, 'Array bidimensional')
print(a.ndim, 'Array unidimensional')

#método para visualizar o formato do array
print('Linhas e colunas', b.shape)

#função para saber o tamanho(primeira dimensão) Mais vale a utilização do .shape
print('Número de linhas', len(b))



print('\n criar automáticamente\n')
#Criar um array com um determinado número de elementos
c = np.arange(0, 11, 1.5)
#np.arange(início, fim(não inclui o número informado), iteração(pode ser float))
print('Array automático, range de 0 a 99\n', c)

#Também permite criar um array uniformemente espaçado, mas diferente do arange vc diz quantos elementos vc quer em um intervalo
d = np.linspace(1, 10, 13)
#(início, término(inclui o número informado), número de itens) ..... se quiser que não inclua o número informado no "término" usar(inicio, término, número de itens, endpoint = False)

print('Array automático entre 1 a 10 com 13 elementos entre eles\n', d)




