# analisando um ano para saber se ele é bissexto ou não

from datetime import date

ano = int(input('Digite um ano para analisar? coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'o ano e bissexto {ano}')
else:
    print('nao bissexto')
