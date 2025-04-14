def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    # Itera sobre cada transação na lista:
    for transacao in transacoes:
        # Verifica se o valor absoluto da transação é maior que o limite:
        if abs(transacao) > limite:
            # Adiciona a transação à lista filtrada:
            transacoes_filtradas.append(transacao)
    return transacoes_filtradas

entrada = input()

entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "")
limite = float(limite.strip())  

transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

resultado = filtrar_transacoes(transacoes, limite)

print(f"Transações: {resultado}")
