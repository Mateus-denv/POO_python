class vendas_blicicletas:
    def __init__(self, cor, modelo, ano, valor): # Construtor
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("plin-plin...")
        
    def parar(self):
        print("Blicicleta parada")
    
    def correr(self):
        print("Blicicleta correndo")
        
    def __str__(self): # Para representações de class
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
b1 = vendas_blicicletas("Azul","kSW","2002","R$ 10.020")
b1.buzinar() # Equivalente a vendas_blicicletas.buzinar(b1)
b1.correr() # Equivalente a vendas_blicicletas.correr(b1)
b1.parar() # Equivalente a vendas_blicicletas.parar(b1)
print(b1.modelo, b1.cor, b1.ano, b1.valor)
print(b1)

b2 = vendas_blicicletas("Preta","Calloi","2025","R$ 100.500")
b2.trocar_marcha()