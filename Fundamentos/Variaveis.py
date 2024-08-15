#nome = 'carlos'
#idade = 26
#profissao = 'programador'

#print(f'Meu nome é {nome} e tenho {idade} e sou um {profissao}') 
# esse 'f' dentro do print serve para podermos fazer a chamada da variavel dentro {}


#print(type(nome)) # str
#print(type(idade)) # int
#print(type(1+2j)) # complex: tipo de dado utilizado em calculos de circuitos eletricos

# Função isinstance
# ela vai pegar a variavel vai verificar o valor se é int e se for retorna true

a = 10
b = 'sol'
print(isinstance(a, int))
print(isinstance(b, int))
print(isinstance(a, (int, float))) # se é um numero real ou ponto flutuante é outra historia, mais é um numero