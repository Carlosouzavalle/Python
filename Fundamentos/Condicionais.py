# simples, composto e encadeado


n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (n1 + n2) / 2

if (media > 7):  # se 
    print('Resultado aprovado')
elif (media >= 5): # senão se / caso contrário, se
    print('Recuperação')
else: # senão
    print('reprovado')