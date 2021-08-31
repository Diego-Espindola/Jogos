lista = [2,4,6,4,3]
palavra = "banana"

#posso usar len(), min() para lista e palavra

#tanto string qnt lista podem ser acessados pelo índex

serie = range(3,10)
print(serie[0])

##lista

dias = ["S", "T", "Q", "Q", "S", "S"]

#Posso adicionar e apagar dados

dias.append("D")#adiciona no último elemento

dias.pop()#apaga o último elemento

print(dias)


#tuple é uma lista que não deve ser alterado

#tuples são parenteses, se eu tentar alterar ele n muda

dias = ("S", "T", "Q", "Q", "S", "S")

##Ele continua sendo possível ser chamado pelo index mas é imutável('tuple' object has no attribute)

dias.lower()