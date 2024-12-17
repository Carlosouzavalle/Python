# adivinha o numero

import random
from time import sleep

#for sorteio in range(1,5):
numero = int(input('Em que numero estou pensando? '))
print('PROCESSANDO...')
sleep(2)
listNumber = [0,1]
#random.choice(listNumber)
if numero == random.choice(listNumber):
    print('Carai tu e brabo')
else:
    print('vish')
    print(random.choice(listNumber))

# pode usar o randint tbm