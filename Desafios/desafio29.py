velo = int(input('Digite a velocidade: '))
valorPermitido = 80
taxa = 7
if velo > valorPermitido:
    valorAjustado = velo - valorPermitido
    valorFinal = taxa * valorAjustado
    # print(valorAjustado)
    # print(valorFinal)
    print(f"Pague multa de {valorFinal}R$ você ultrapassou o limite de {valorPermitido}km/h")
    print("Boa Viagem!!!")

else:
    print("Tudo certo boa viagem!!!")