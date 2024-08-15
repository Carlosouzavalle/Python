# + soma
# - subtração
#  / divisão
#  * multiplicação
#  // divisão inteira 
#  % modulo
# ** potencia


# a = 10
# b = 3
# print(a // b)
# print(a % b) 
# print(a / b)
# print(a * b)
# print(a + b)
# print(a - b)
# print(a ** b)


# porem se quisermos fazer mais de uma operação e priorizar uma especifica?

print(3 + 2 * 4) # ele vai fazer 4 * 2 = 8 e depois + 3 = 11
print((3 + 2) * 4) # 20 priorizamos o 3 + 2

a = int(input('Digite um numero? '))
b = int(input('Digite outro numero? '))
# int(input('Digite outro numero? ')) isso se chama casting
# ou seja o valor vai ser convertido em int antes de ser adicionado a variavel

resultado = a + b
print(f'a soma de {a} + o numero {b} é {resultado}')