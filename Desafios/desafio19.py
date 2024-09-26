# sorteando un item da lista

import random

for valor in range(1, 5):
    item = input('Digite um nome: ')

lista = []
lista.append(item)

sorteando = random.choice(lista)
print(sorteando)

# choice = Retorna um elemento aleatório da sequência não vazia seq. Se seq estiver vazio, levanta IndexError.