ContaCorrente = 0
qtd_saques = 3
ValorDeSaque = 0
     

while True:
        mensagemBoasVindas = input("Escolha uma opção 1: Deposito e 2: Saque ")

        if mensagemBoasVindas == "1":
            
            ValorDeDeposito = float(input("Qual valor você quer depositar? "))
            if ValorDeDeposito <= 0:
                print("ERRO!!! O Valor informado não é valido.")
            else:
                ContaCorrente += ValorDeDeposito
                print(f"Seu saldo é de {ContaCorrente}R$ ")

       
        elif mensagemBoasVindas == "2":  
                if qtd_saques == 0:
                    print("por hoje deu pai volta amanha")
                else:
                    ValorDeSaque = float(input("qual valor você quer sacar? "))
                    if ValorDeSaque <= 0:
                        print("ERROR!!! valor invalido")
                    elif ValorDeSaque > ContaCorrente:
                        print("ERRO!!! Saldo insuficiente.")
                    else:
                        ContaCorrente -= ValorDeSaque
                        qtd_saques -=1
                        print(ContaCorrente)
                    
