# saida de dados com função print, format e f-string

msg = 'Funcao print()'
print('a msg e ', msg)

# nome = input('Digite seu nome? ')
# print(f'Olá {nome}')


#  print('Imprime a msg e permanece na linha', end='')
#  print('vai ficar na msm linha')
#  end=''  isso aqui significa que não é para ter quebra de linha


nome = 'Carlos'
idade = 26
msg_formatada = 'O nome e {0} e ele tem {1} anos'.format(nome, idade)
print(msg_formatada)
# .format(nome, idade)  vamos por pela posição agora primeiro o nome e depois a idade


valor = 123.321123
print(f'o valor é  {valor:.2f}')
print(f'o valor é  \'{valor:.2f}\' ')

#  {valor:.2f}  duas casas decimais
#  \'{valor:.2f}\'  estamos dizendo para ele não interpretar isso como as aspas da f-string


print(f'Nome: \t{nome}\t Idade: \t{idade}')
# \t  outro caracter de escape, uma tabulação