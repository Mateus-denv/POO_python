class Animal():
    # Construtor da classe Animal, recebe número de patas
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas  # Atributo da instância

    # Método especial para representação em string do objeto
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"  

class Manimeros(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo          # Define atributo cor_pelo
        
        # Chama o construtor da superclasse (Animal)
        super().__init__(**kw)  # Usa **kw para capturar argumentos adicionais e repassá-los para o super().__init__().      
        
class Aves(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico         
        super().__init__(**kw)    

class Gato(Manimeros):
    pass

class Onitorrinco(Manimeros, Aves):
    pass

# Cria uma instância da classe Gato
gato = Gato(cor_pelo="azul", nmr_patas=4) 

# Imprime a representação do objeto gato
print(gato) 

onitorrinco = Onitorrinco(cor_pelo="cinza", cor_bico="cinza", nmr_patas=4)

print(onitorrinco)  # Saída: Onitorrinco:cor_pelo=cinza, nmr_patas=4
# Nota: cor_bico não aparece pois Aves.__init__ não foi chamado!
