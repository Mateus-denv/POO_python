class Estudante:
    # Variável de classe: compartilhada por todas as instâncias da classe
    escola = "Dio"
    
    def __init__(self, nome, matricula):
        # Variáveis de instância: únicas para cada objeto (instância) da classe
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self) -> str:
        # Note que 'self.escola' acessa a variável de classe, pois não foi definida como instância
        return f"Nome:{self.nome} Matricular: {self.matricula} Escola: {self.escola}"
    
def mostrar(*objetos):
    for obj in objetos:
        print(obj)    
        
aluno_1 = Estudante("Mateus", 1120)
aluno_2 = Estudante("João", 1128)

mostrar(aluno_1, aluno_2)

# Aqui ocorre a mudança da variável de classe 'escola' para todas as instâncias
Estudante.escola = 'Alura'

# Modificação da variável de instância 'matricula' apenas para o aluno_2
aluno_2.matricula = 1234

mostrar(aluno_1, aluno_2)
