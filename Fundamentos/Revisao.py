# maneira mais comum
#frutas = ["apple", "grape", "Guava"]
#print(frutas[2])

# Adiciona um item ao fim da lista.
#frutas.append("tomate")
#print(frutas)

# list.extend = The extend() method adds the specified list elements (or any iterable) to the end of the current list.

#vegetables = ["carrots", "anios", "Pumpkin"]

#frutas.extend(vegetables)
#print(frutas)

# juntado duas lista em uma só
#ewList = frutas + vegetables
#print(newList)

# Insere um item em uma dada posição. O primeiro argumento é o índice do elemento antes do qual será feita a inserção, assim a.insert(0, x)
#frutas.insert(2,"water melon")
#print(frutas)



# operadores de identidade

#saldo = 1000
#limite = 500

#print(saldo is limite) # eles não ocupam a mesma regiao de memoria
#print(saldo is not limite)


#print("orange" in frutas)
#print("orange" not in frutas)



# laço de repetição 
# for

# for i in range(10):
#     print(i)


# while

# num = 0
# while (num <= 10):
#     num += 1
#     print(num)
    
    

# args e kwargs
# def calcular_imposto(valor, perc_ir):
#     ir = valor * perc_ir
#     iss = valor * 0.05
#     csll = valor * 0.0375
#     piss = valor * 0.03
#     return ir + iss + csll + piss

# print(calcular_imposto(1000, 0.275))






# STRINGS 

#NOME = "carlos";
#print(NOME.upper()) # fica tudo maiuscula
#print(NOME.lower()) # tudo minuscula 
#print(NOME.title()) # primeira letra maiuscula 


#texto = "       Hello world!    "
#print(texto)
#print(texto.strip()) # remove os esáços do começo e do fim do texto
#print(texto.replace(" ", "")) # remove todos os espaços 
#print(texto.lstrip()+ ".") # remove espaços a esquerda
#print(texto.rstrip()+ ".") # remove os espaços a direita



#texto2 = "Hello world"
#print(texto2.center(13,"#"))


#print(".".join(texto2))


# strings de multiplas linhas

#frase = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

#print(frase)


## TUPLAS 
## A diferença de tupla e listas é que 
# tuplas são imutaveis
# listas são mutaveis 

#frutas = ("uva", "maça", "tomate")
#print(frutas)



## CONJUNTOS    

# numeros = set([1,2,3,4,5])
# print(numeros)

# carros = set(("palio", "gol", "uno"))
# print(carros)

# linguagens = {"javascript", "C#", "Python"}
# print(linguagens)

# METODOS DO CONJUNTO
















# DICIONARIO

contatos = {
    "caca123@lala.com": {"nome": "Caca", "telefone": "123123123"},
    "jaja123@lala.com": {"nome": "Caca", "telefone": "123123123"},
    "lala123@lala.com": {"nome": "Caca", "telefone": "123123123"}
}

telefone = contatos["jaja123@lala.com"]["telefone"]
print("Telefone: " + telefone)

nome = contatos["jaja123@lala.com"] 
print(nome)