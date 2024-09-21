#crie um algoritmo que leia o preço de um produto e apresente ele com 5% de desconto


preco = float(input('Digite o preço do produto? R$')) 
desconto = preco * (5 / 100)
preco_com_desconto = preco - desconto
print(f'o resultado é R${preco_com_desconto :.2f}')