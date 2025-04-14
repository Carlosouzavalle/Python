def calcular_saldo(transacoes):
    saldo = sum(transacoes)
    return saldo

# Entrada do usuário
entrada = input().strip()

# Processamento da entrada
# Remove os colchetes e espaços extras, depois divide pelas vírgulas
transacoes_str = entrada.strip('[]').replace(' ', '').split(',')

# Converte os valores para float, ignorando strings vazias
transacoes = []
for valor in transacoes_str:
    if valor:
        transacoes.append(float(valor))

# Calcula o saldo
saldo_final = calcular_saldo(transacoes)

# Formata a saída
print(f"Saldo: R$ {saldo_final:.2f}")