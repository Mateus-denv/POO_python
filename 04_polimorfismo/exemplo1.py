class Passaros():
    def voar(self): pass
    
class Pardal(Passaros):
    def voar(self):
        print("Pardal pode voar")
        pass
        
class Avestruz(Passaros):
    def voar(self):
        print("Avestruz não pode voar")
        
def plano_de_voo(passaro):
    passaro.voar()
    pass

plano_de_voo(Pardal())
plano_de_voo(Avestruz())