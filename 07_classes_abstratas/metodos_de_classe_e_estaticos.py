class Pessoa():
    # Construtor: define os atributos de instância
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        
    # Método de classe: recebe a própria classe como primeiro parâmetro (cls), utilizad quando preciso ter acesso ao contexto da classe.
    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        print(cls)  # Mostra a referência à classe (Pessoa)
        
        # Retorna uma nova instância da classe Pessoa usando os valores calculados
        return cls(nome, idade)
    
    # Método estático: não recebe nem self nem cls; é uma função utilitária dentro da classe, utilizado quando não precisamos nem de contexto, nem de classe e nem da instacia do objeto.
    @staticmethod
    def maior_de_idade(idade):
        maior = True if idade >= 18 else False
        return maior    
    
p = Pessoa("Mateus", 22)
print(p.nome, p.idade)

# Criação de uma instância usando o método de classe
p1 = Pessoa.criar_data_nascimento(2003, 2, 3, "Mateus")
print(p1.idade, p1.nome)

# Uso do método estático: verifica se a idade representa um adulto
print(Pessoa.maior_de_idade(28))  # True
print(Pessoa.maior_de_idade(12))  # False
