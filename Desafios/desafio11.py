# faça um programa que receba a altura e a largura mostre o tamanho e m² e quantos litros de tinta precisa para pintar

altura = float(input('Qual a altura? '))
largura = float(input('Qual a largura? '))
metros_quadrados = altura * largura
litros = metros_quadrados / 2
print(f'Sua parede tem as dimesão de {altura}x{largura} e sua area é de {metros_quadrados}m²')
print(f'Para pintar a parede você vai precisar de {litros}l')