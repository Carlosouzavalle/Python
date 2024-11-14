# Separando dígitos de um número

valor = int(input('digite um valor: '))
print(f'analisando o {valor}')
uniValor = valor % 10
print(f'tem {uniValor} unidades')
valor = (valor - uniValor) / 10
dezena = valor % 10
valor = (valor - dezena) / 10
centena = valor % 10
valor = (valor - centena) / 10
milhar = valor % 10

print(f'tem {dezena: .0f} dezenas')
print(f'tem {centena: .0f} centena')
print(f'tem {milhar: .0f} milhar')