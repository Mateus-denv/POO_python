class Pessoa():
    # Construtor da classe com nome e ano de nascimento
    def __init__(self, nome, ano_nascimento):
        self._nome = nome  # Atributo protegido _nome
        self._ano_nascimento = ano_nascimento  # Atributo protegido _ano_nascimento
        
    # Cria uma propriedade de leitura para acessar o nome
    @property
    def mostrar_nome(self):
        return self._nome  # Retorna o nome (sem usar método direto)
    
    # Cria uma propriedade para calcular a idade com base no ano atual
    @property
    def idade(self):
        _ano_atual = 2025  # Ano atual fixo
        return _ano_atual - self._ano_nascimento  # Calcula a idade
    
    # Define um setter (modificador) para o nome — embora ainda sem lógica implementada
    @mostrar_nome.setter
    def mostrar_nome(self, value):
        # Lógica para modificar o nome (não implementada ainda)
        pass

# Cria uma instância da classe Pessoa
pessoa = Pessoa("Mateus de Jesus Santos Costa ", 2005)

# Imprime o nome e a idade da pessoa usando as propriedades
print(f"{pessoa.mostrar_nome}\n{pessoa.idade}")
