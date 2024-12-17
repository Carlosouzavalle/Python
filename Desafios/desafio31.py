# custo de viagen cobra 50 centavos por viagens até 200km e 45 por mais longas 

distancia = int(input('Qual a distancia da viagem? '))
desconto = 200
valorPorKM = 0.50
valorPorKMacimade200 = 0.45

if distancia > desconto:
    precoFinal = valorPorKMacimade200 * distancia
    print(f' Sua viagem com preço promocional {precoFinal}R$ ')
else: 
    precoFinal = valorPorKM * distancia 
    print(f' O preço da sua viagem vai custar {precoFinal}R$ ')
    