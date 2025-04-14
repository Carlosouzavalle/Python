class loja():
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def parar(self, parar):
        self.parar = parar  
        
    def buzinar(self, buzinar):
        self.buzinar = buzinar
        
    def correr(self, correr):
        self.correr = correr


Bike1 = loja("Vermelha", "Caloi", 2022, 1200.00)
print(Bike1.cor)


Bike1.buzinar("biiiii")   
Bike1.correr("A bicicleta esta em movimento")
print(Bike1.buzinar)
print(Bike1.correr)