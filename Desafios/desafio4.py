valor = input('Digite algo? ')

print('o tipo do valor é ', type(valor))
print('só tem espaços? ', valor.isspace())
print('é um numero? ', valor.isnumeric())
print('é alfabetico? ', valor.isalpha())
print('é alfanumerico? ', valor.isalnum())
print('esta em maiusculo? ', valor.isupper())
print('esta em minusculo? ', valor.islower())
print('esta capitalizado? ', valor.istitle()) # capitalizado