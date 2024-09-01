#escreva um programa em metros e mostre ele em outras medidas

valor = float(input('Digite uma distancia em metros: '))
km = valor / 10 / 10 / 10
hm = valor / 10 / 10
dam = valor / 10
dm = valor * 10
cm = valor * 10 * 10
mm = valor * 10 * 10 * 10
print(f'a medida em km é {km}')
print(f'a medida em hm é {hm}')
print(f'a medida em dam é {dam}')
print(f'a medida em dm é {dm}')
print(f'a medida em cm é {cm}')
print(f'a medida em mm é {mm}')