# faça um programa que mostre os seguintes resultados de um determinado valor 
# (tipo, se tem espaços, se é um numero, se é alfabético, se é alfanumerico, se esta em maiusculp, se esta em minusculo, e se esta capitalizado ) 

valor = input('Digite algo? ')


print('o tipo do valor é ', type(valor))
print('só tem espaços? ', valor.isspace())
print('é um numero? ', valor.isnumeric())
print('é alfabetico? ', valor.isalpha())
print('é alfanumerico? ', valor.isalnum())
print('esta em maiusculo? ', valor.isupper())
print('esta em minusculo? ', valor.islower())
print('esta capitalizado? ', valor.istitle()) # capitalizado