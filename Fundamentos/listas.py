# listas

# Uma lista em Python é uma estrutura de dados que armazena uma sequência de valores. As listas em Python 
# são classificadas como um tipo de dado mutável, e portanto não possuem tamanho fixo: podemos adicionar ou 
# remover elementos de listas de maneira dinâmica ao longo do código.


lista_de_numeros = [1,2,3]
lista_de_clientes = ['carlos', 'bia', 'fernanda']


print(lista_de_clientes[0])
print(lista_de_clientes)

print(lista_de_numeros[0])
print(lista_de_numeros[1])
print(lista_de_numeros[2])

# alterando o valor do indice 0
lista_de_numeros[0] = 5

print(lista_de_numeros[0])




# methods 


lista_vazia = []

lista_vazia.append('ola')
print(lista_vazia)

lista_vazia.insert(2, 'carlos') # insere um novo item na posição dada
print(lista_vazia)

lista_vazia.pop() # remove o ultimo item da lista
print(lista_vazia) 

lista_de_clientes.pop(1) # remove o elemento da posição
print(lista_de_clientes) 



frutas = ['maça', 'laranja', 'uva']

frutas.remove("maça") # vai remover o elemento selecionado 
print(frutas)

frutas.reverse() # ele vai inverter os elementos da lista
print(frutas)


numeros = [1,2,3,4,5]
numeros2 = [6,7,8,9,10]
numeros.extend(numeros2) # adiciona elementos especificos de uma lista em outra
print(numeros)


numeros.clear() # remove todos os elementos de uma lista
print(numeros)

x = frutas.copy() # retorna uma copia de uma lista especifica
print(x)


y = len(frutas) # retorna o numero de elementos de uma lista
print(y)