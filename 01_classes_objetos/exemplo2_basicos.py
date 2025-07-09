class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a class")

        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    def falar(self):
        print("AU")
        
    def __del__(self):
        print("Removendo instancia da class")
        
def criar_cachorro():
    c = Cachorro("caramelo","marrom",False)
    print(c.nome)

        
c1 = Cachorro("pretinho","preto")
c1.falar()
 
print("Olá mundo")
del c1
print("Olá mundo")
print("Olá mundo")
print("Olá mundo")
print("Olá mundo")
