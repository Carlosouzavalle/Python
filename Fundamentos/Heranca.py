class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas 
    
    def ligar_motor(self):
        print("Ligando o motor")
        
    def __str__(self):
        return f"{self.__class__.__name__}(Cor:{self.cor}, Placa: {self.placa}, Rodas: {self.numero_rodas})"

class Motocicleta(Veiculo):
    pass 

class carro(Veiculo):
    pass

class camihnao(Veiculo):
    pass


moto = Motocicleta("preta", "JK2HG", 2) 
print(moto)
caminhao = camihnao("Branco", "JKG24H", 8)
print(caminhao)