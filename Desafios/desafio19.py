# sorteando un item da lista

import random

for valor in range(1, 5):
    item = input('Digite um nome: ')

lista = []
lista.append(item)

sorteando = random.choice(lista)
print(sorteando)

