# crie um programa e diga se ela começa ou não com o nome santo

valor = input('Qual cidade você nasceu? ').strip()

if valor.upper().startswith('SANTO'):
    print(True)
else:
    print(False)