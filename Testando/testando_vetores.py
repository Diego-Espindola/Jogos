random_nome = (('queijo').lower()).strip()
nome_secreto = []*len(random_nome)


for c in range(0, len(random_nome)):
    nome_secreto[c] = random_nome[c]
    print(nome_secreto[c])
