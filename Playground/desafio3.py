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
        
    # def __str__(self):
    #     return f"Bicicleta: Cor={self.cor} Modelo={self.modelo} Ano={self.ano} Valor={self.valor}"


    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

Bike1 = loja("Vermelha", "Caloi", 2022, 1200.00)
print(Bike1)


Bike1.buzinar("biiiii")   
Bike1.correr("A bicicleta esta em movimento")
print(Bike1.buzinar)
print(Bike1.correr)