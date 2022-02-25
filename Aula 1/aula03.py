# Operadores

# Ordem de precedência
# 1 ()
# 2 **
# 3 * / // %
# 4 + -

# ex
# 5 + 3 * 2 = 11

# porem se quisermos fazer exatamente como esta sendo apresentado
# print(5 + 3 * 2) # errado entre aspas
# print((5 + 3) * 2) # certo

n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
s =  n1 + n2
m = n1 + n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, \n o produto é {} e a \n divisão é {:.1f}'. format(s, m, d), end=' ')
print('divisão inteira {} e potencia {}' .format(di, e))

# {:.1f} vai fazer com que algum numero muito grande diminua a quantidade de cassas decimais
# ex: 4 por 3 sua divisão inteira dara 1.3333333333333333 muito grande então usamos o 
# {:.1f} para reduzilo e assim fica 1.3
# end=' ' para não quebrar a linha 
# \n para quebrar a  linha