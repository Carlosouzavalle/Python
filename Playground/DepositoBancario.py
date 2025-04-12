ContaCorrente = 0
qtd_saques = 3
qtd_deposito = 3
ValorDeSaque = 0

     

                                 
def deposito():
        global ContaCorrente, qtd_deposito 
        
        if qtd_deposito == 0:
            print("Limite de transações excedido!!!")
            return
        
        ValorDeDeposito = float(input("Qual valor você quer depositar? "))
        if ValorDeDeposito <= 0:
            print("ERRO!!! O Valor informado não é valido.")
        else:
            ContaCorrente += ValorDeDeposito
            qtd_deposito -=1
            print(f"Seu saldo é de {ContaCorrente}R$ ")
            print(f"Depósitos restantes hoje: {qtd_deposito}")
        Menu()
        
        
              
def saque():
    global qtd_saques, ContaCorrente
    
    for s in range(5):
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
    Menu()
                
                                
def Abrir_conta():
    cliente = {
        "NAME":  input("Qual seu nome? "),
        "AGE":  int(input("Quantos anos  você tem? "))
    }
    return cliente
    
    
def Usuario(usuario):
    print(f"Seja Bem-Vindo(a) {usuario['NAME']}")


                
                
def Menu():
    mensagemBoasVindas = input("Escolha uma opção 1: Deposito?  2: Saque?  3: Abrir Conta? ")                     

    if mensagemBoasVindas == "1":
        deposito()
    elif mensagemBoasVindas == "2": 
        saque()
    elif mensagemBoasVindas == "3":
        #Abrir_conta()
        usuario = Abrir_conta()
        Usuario(usuario)
    else:
        print("Opção invalida")

Menu()