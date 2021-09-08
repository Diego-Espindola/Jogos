import numpy as np
print('Criando manualmente')
a = np.array([0, 1, 2, 3])
print('a: array\n', a)

b = np.array([[0, 1, 2], [3, 4, 5], [5, 6, 7], [8,9,10]])

#possui duas linhas, cada lista interna é uma linha, e cada item é uma coluna 4x3

print('b:array com lista bidimensional\n', b)
print()


#como saber a dimensão do array
print(b.ndim, 'b.ndim: Array bidimensional')
print()
print(a.ndim, 'a.ndim: Array unidimensional')
print()
#método para visualizar o formato do array
print('b.shape: Linhas e colunas', b.shape)
print()
#função para saber o tamanho(primeira dimensão) Mais vale a utilização do .shape
print('len(b): Número de linhas', len(b))
print()


print('\n criar automáticamente\n')
#Criar um array com um determinado número de elementos
c = np.arange(0, 11, 1.5)
#np.arange(início, fim(não inclui o número informado), iteração(pode ser float))
print('c: Array automático, range de 0 a 11 com um intervalo de 1.5\n', c)
print()
#Também permite criar um array uniformemente espaçado, mas diferente do arange vc diz quantos elementos vc quer em um intervalo
d = np.linspace(1, 10, 13)
#(início, término(inclui o número informado), número de itens) ..... se quiser que não inclua o número informado no "término" usar(inicio, término, número de itens, endpoint = False)

print('d: Array automático entre 1 a 10 com 13 elementos entre eles\n', d)
print()

#Criar array de 1s

e = np.ones(10)
print('e: Array de 10 1s', e)
print()

#Criar array que seja uma matriz
f = np.ones((3,3))
print('f: Array Matriz 3x3\n', f)
print()

#da mesma forma com zeros, pode trocarnp.ones por np.zeros (Funciona tanto uni qnt bidimensional)

g = np.zeros(4)
print('g: Array unidimensional de zeros\n', g)
print()

#array de números aleatórios
h = np.random.rand(10)
print('h: 10 números aleatórios entre 0 e 1')
print()

i = np.random.rand(3, 3)
print('')





