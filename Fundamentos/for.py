# laço de repetição for

num = 0

for valores in range(10): # Loop de 0 a 9, totalizando 10 iterações
    num += 1 
    print(valores)

# o for funciona diferente de outras linguagens

print('================================================================')

nome = 'Carlos'
for letras in nome:
    print(letras)


lista = [1,2,3,4,5,6]
for items in lista: 
    print(items)


# encadeando laços 

for cont_ex in range(1, 6):
    print(f'\nRodada: {cont_ex}')
    for cont_int in range(5,0, -1):
        print(f'Valor: {cont_int}')
print('fim dos laços')



# poderia ser o resultado de uma loteria por exemplo
import random

for A in range(1,6):
    print(f'\nConjunto {A}')
    for B in range(5):
        num = random.randint(1,100)
        print(f'Valor: {num}')