# maneira mais comum
frutas = ["apple", "grape", "Guava"]
#print(frutas[2])

# Adiciona um item ao fim da lista.
frutas.append("tomate")
#print(frutas)

# list.extend = The extend() method adds the specified list elements (or any iterable) to the end of the current list.

vegetables = ["carrots", "anios", "Pumpkin"]

#frutas.extend(vegetables)
#print(frutas)

# juntado duas lista em uma só
newList = frutas + vegetables
print(newList)

# Insere um item em uma dada posição. O primeiro argumento é o índice do elemento antes do qual será feita a inserção, assim a.insert(0, x)
frutas.insert(2,"water melon")
print(frutas)



# operadores de identidade

saldo = 1000
limite = 500

print(saldo is limite) # eles não ocupam a mesma regiao de memoria
print(saldo is not limite)


print("orange" in frutas)
print("orange" not in frutas)