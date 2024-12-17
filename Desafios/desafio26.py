# quantas vezes aparece "x" letra

frase = str(input('Digite uma frase: '))
print('a letra A aparece', frase.upper().count('A'), 'vezes.')
print('a letra A aparece primeiro', frase.upper().find('A'))
print('a letra A aparece primeiro', frase.upper().rfind('A'))