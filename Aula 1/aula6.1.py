# Tupla

# diferença entre lista e tupla 
# tupla é imutavel
# lista é mutavel 
# isso é com a lista podemos manipular seus valores com a tupla não

lista_animais = ['gato', 'cachorro', 'elefante', 'lobo', 'arara']
tupla = (1, 10, 12, 14)
print(tupla)
print(len(tupla))
# da pra fazer a mesma coisa com a lista 
print(len(lista_animais))

# convertendo uma lista para uma tupla

tuple_animal = tuple(lista_animais)
print(tuple_animal)

# convertendo uma tupla para uma lista
lista_numerica = list(tupla)
print(lista_numerica)