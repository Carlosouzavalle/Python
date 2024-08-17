# laço de repetição
# vai repetir até que uma determinada confição seja atendida e ele finalize a execução

# num = 1

# while(num <= 10):
#     print(num)
#     num += 1
# print('fim do laço')



nome = None

while True:
    print('Digite seu nome ou X para parar: ', end='')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Olá bem-vindo, {nome}')
print('Até logo!')