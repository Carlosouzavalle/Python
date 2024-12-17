# qual é o numero maior e o menor 

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
numeros = [n1, n2, n3]

# if n1 > n2:
#     print(f'{n1} é maior que {n2}')
# elif n1 > n3:
#     print(f'{n1} é maior que {n3}')
# elif n2 > n3:
#     print(f'{n2} é maior que {n3}')


print(f'O maior valor digitado foi  { max(numeros) }')
print(f'O menor numero digitado foi { min(numeros) }')