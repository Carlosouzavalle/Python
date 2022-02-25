variavel1 = input('Digite algo: ')
print('O tipo primitivo é',type(variavel1))

print('so tem espaços? {}' .format(variavel1.isspace()))
# print('so tem espaços?',variavel1.isspace())
print('é um numero? ', variavel1.isnumeric())
print('é alfabético? ', variavel1.isalpha())
print('é alfanumerico? ', variavel1.isalnum())
print('esta em maiúsculas? ', variavel1.isupper())
print('esta em minúsculas? ', variavel1.islower())
print('esta capitalizada? ', variavel1.istitle())

# a small different way to write in frist line using .format()