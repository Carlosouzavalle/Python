# lista aleatoria

import random
lista = []

for ordem in range(1, 4):
    nome = input('Digite o nome do aluno: ')
    lista.append(nome)
    random.shuffle(lista)

print(lista)

# shufle = Embaralha a sequência x internamente.