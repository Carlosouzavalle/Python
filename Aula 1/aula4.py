# if, elif, and,else, or e not
# em python o : determina o abrimento do bloco
# e tudo que estiver tabiado dentro do bloco esta dentro do if
# o not ele inverte a condição parecido com o ! nas outras linguagens

#=================================================================================================================

# a = int(input('Digite um valor: '))
# b = int(input('Digite outro valor: '))
# c = int(input('Terceiro valor: '))

# if a > b and a > c:
#     print('O numero {} é maior' .format(a))
# elif b > a and b > c:
#     print('O maior numero é {}' .format(b))
# else:
#     print('o maior numero é {}' .format(a))
# print('final do programa')

#=================================================================================================================

# a = int(input('Digite um valor: '))
# b = int(input('Digite outro valor: '))

# resto_a = a % 2
# resto_b = b % 2 

# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um numero par')
# else:
#     print('nenhum numero par digitado')

#=================================================================================================================

a = int(input('Nota do primeiro Bimestre: '))
b = int(input('Nota do segundo bimestre: '))
c = int(input('Nota do terceiro Bimestre: '))
d = int(input('Nota do quarto Bimestre: '))
media = (a + b + c + d) / 4

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('A sua media é {}' .format(media))
else:
    print('Houve um Erro inesperado')


    
