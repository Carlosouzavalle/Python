# crie um algoritmo que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelo 
# qual foi alugado. sendo que o preço a pagar é 60R$ por dia e 0,15R$ por km rodado


km_percorrido = float(input('Quantos km percorridos? '))
dias_alugados = float(input('Quantos dias alugados? '))

valor_por_km = 0.15
valor_por_dia = 60

resultado = valor_por_km * km_percorrido + valor_por_dia * dias_alugados
print(resultado)