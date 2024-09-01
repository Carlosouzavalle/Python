# faça um programa que leia um valor e apresente sua tabuada

# com while
# valor = int(input('Digite um numero? '))
# valor2 = 0
# while(valor2 <= 9):
#     valor2 += 1
#     resultado = (valor * valor2)
#     print(f'{valor} X {valor2} = {resultado}' )


# com o for 
valor = int(input('Digite um numero? '))
for valor2 in range(11):
    resultado = valor * valor2
    print(f'{valor} X {valor2} = {resultado}' )
