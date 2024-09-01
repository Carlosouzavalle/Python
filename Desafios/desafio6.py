#crie um algoritmo que mostre o dobro, o triplo e a raiz

valor = int(input('digite o valor: '))
a = valor * 2
b = valor * 3
c = valor ** (1/2)

print(f'o dobro é {a}')
print(f'o triplo é {b}')
print('a raiz-quadrada é {:.2f}'.format(c))

# pow() calcula raiz quadrada tbm