class Veiculo():
    pass
    def __init__(self,cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas =  numero_rodas
    def ligar_motor(self):
        print("Motor ligado")
        
    def __str__(self): # Para representações de class
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"    
    
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas,carregado):
        super().__init__(cor, placa, numero_rodas)
        
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"Está carregado" if self.carregado == True else "Não está carregado")
        
class Aviao(Veiculo):
    pass

moto = Motocicleta(cor="preto",placa="1234abcd",numero_rodas="2")

carro = Carro(cor="azul",placa="bcds",numero_rodas="4")

caminhao = Caminhao(cor="verde",placa="1234csde",numero_rodas="6",carregado=False)

aviao = Aviao(cor="branco",placa="1234ergf",numero_rodas="2")

moto.ligar_motor()
carro.ligar_motor()
caminhao.ligar_motor()
caminhao.esta_carregado()
aviao.ligar_motor()

print(moto)
print(carro)
print(caminhao)
print(aviao)