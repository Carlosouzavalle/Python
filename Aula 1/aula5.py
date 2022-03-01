# LOOPS

# LAÇO FOR

# a = int(input('Digite um valor: '))

# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div = div +1

#     if div == 2:
#         print('Numero {} é primo' .format(a))
#     else:
#         print('numero {} não é primo' .format(a))

#=============================================================================================================

# LAÇO FOR

# for num in range(101):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div +=1
#     if div == 2:
#         print(num)

#=============================================================================================================

# While

nota = int(input('Digite uma nota: '))

while nota > 11:
    nota = int(input('ERROR!!! A é nota Invalida: '))