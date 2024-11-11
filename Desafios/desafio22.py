nome = input('Digite seu nome: ').strip()
novoNome = nome.upper()
novoNome2 = nome.lower()
novoNome3 = len(nome) - nome.count('  ')

print(f'Seu nome em maiuscula fica: {novoNome}')
print(f'Seu nome em minuscula fica: {novoNome2}')
print(f'Seu nome tem {novoNome3} letras')
print(f'Seu nome é {nome} e tem  {novoNome3} letras ')