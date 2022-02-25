# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
rq = n ** 2
print('O dobro de {} é: {}' .format(n, d))
print('O triplo de {} é: {}' .format(n, t))
print('A raiz quadrada de {} é: {}' .format(n, rq))


# Resposta do professor
n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é: {}' .format(n, d))
print('O triplo de {} é: {}' .format(n, t))
print('A raiz quadrada de {} é: {:.2f}' .format(n, r))