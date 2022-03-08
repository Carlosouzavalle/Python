#  Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite o valor em métros: '))
milimetros = metros * 1000
centimetros = metros * 100
# print('%10.3f metros equivalem a %10.3f milimetros.' % (metros, milimetros))
# print('%10.2f metros equivalem a %10.2f centimetros' % (metros, centimetros))
print('A quantidade de {} metros equivale a {} centimetros e {} em milimetros'  .format(metros, centimetros, milimetros))