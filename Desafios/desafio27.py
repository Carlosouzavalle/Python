#primeiro nome e ultimo nome

# nome = str(input('digite seu nome: '))
# print(f'seu primeiro nome é ', nome[0:6])
# print(f'seu sobrenome é ', nome[7::])

# minha solução funciona se  o nome for pequeno 

n = str(input('Digite o seu nome: ')).strip()
nome = n.split()
print('Seu primeiro nome é',nome[0])
print('Seu ultimo nome é',nome[len(nome)-1])