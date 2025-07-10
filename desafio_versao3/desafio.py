# @staticmethod: O método não precisa acessar atributos da instância nem da classe.

# Importa classes base para herança abstrata e manipulação de datas e fuso horário
from abc import ABC, abstractmethod
from datetime import datetime, timedelta, timezone

# Classe base Conta (geral)
class Conta():
    
    def __init__(self, saldo, numero, agencia, cliente, historico): 
        # Inicializa os atributos da conta
        self._numero = numero # Número da conta (int)
        self._agencia = agencia # Código da agência (str)
        self._cliente = cliente # Cliente da conta (instância da classe Cliente)
        self._historico = historico # Histórico da conta (instância da classe Historico)
        
    @property
    def get_saldo(self):
        return self._saldo
        
    @get_saldo.setter
    def set_saldo(self, valor):
        self._saldo = valor # Saldo da conta (float)
         

    def nova_conta(self, cliente):
        # Atribui um novo cliente à conta
        self._cliente = cliente

    def sacar(self, valor):
        # Método placeholder para saque (a ser implementado)
        ...
    
    def depositar(self, valor):
        # Método placeholder para depósito (a ser implementado)
        ...

# Classe Cliente (abstração de um cliente do banco)
class Cliente():
    def __init__(self, endereco, contas):
        self._endereco = endereco        # Endereço do cliente (str)
        self._contas = contas            # Lista de contas associadas ao cliente

    def realizar_transacao(self, conta, transacao):
        # Registra uma transação realizada
        self._conta = conta
        self._transacao = transacao
        
    def adicionar_cliente(self, conta):
        # Associa uma conta a esse cliente
        self._conta = conta

    def conta_exite(cpf_informado, contas = [["10361795599"]]):
        # Verifica se existe uma conta com o CPF informado
        for conta in contas:
            if conta[0] == cpf_informado:
                return True

# Classe ContaCorrente, herda de Conta
class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        # Reaproveita o construtor da classe base
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite                    # Limite de crédito
        self._limites_saques = limite_saques     # Número de saques permitidos

# Pessoa Física herda de Cliente e adiciona atributos específicos
class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento):
        super().__init__(endereco, contas)
        self._cpf = cpf                          # CPF do cliente
        self._nome = nome                        # Nome do cliente
        self._data_nascimento = data_nascimento  # Data de nascimento

# Interface abstrata para transações
class interfaceTransacao(ABC):

    @abstractmethod
    def registrar_transacao(conta):
        # Método que será obrigatório em subclasses
        ...

# Classe de depósito implementando a interface de transação
class Deposito(interfaceTransacao):
    _valor = 0  # Valor da transação

    def __init__(self, valor):
        self._valor = valor  # Valor passado no construtor

    def registrar_transacao(conta):
        # Método a ser implementado
        ...    

# Classe de saque implementando a interface de transação
class Saque(interfaceTransacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar_transacao(conta):
        # Método a ser implementado
        ...

# Classe de histórico de transações
class Historico: 
    def __init__(self, transacao):
        self.transacao = transacao  # Lista ou registro de transações

    def adicionar_transacao(self):
        # Método a ser implementado
        ...

# Validador de informações
class Validador:
  
    @staticmethod
    def validar_cpf(cpf):
        # Verifica se o CPF tem apenas números e 11 dígitos
        if not cpf.isdigit() or len(cpf) != 11:
            return False
        else:
            return True

# Classe para exibir menus da aplicação
class Menu:
    @staticmethod 
    def exibir_inicial():
        # Exibe o menu inicial para o usuário
        print("[L] Logar na conta")       
        print("[C] Criar conta")

        opcao = input(">>> ").upper()       # Entrada do usuário, convertida para maiúscula
        return opcao

    @staticmethod    
    def exibir_principal():
        # Menu principal da conta após login
        print("[R] Criar conta corrente")
        print("[D] Depositar")
        print("[S] Sacar")
        print("[V] Ver saldo")
        print("[E] extrato")
        print("[Q] Sair")
        
        opcao = input(">>> ").upper()
        return opcao
    
# Classe para exibir o login 
class Login():
    @staticmethod
    def logar_conta():
        cpf = input("Digite o CPF do proprietário da conta (apenas números):\n>>> ")
        if Validador.validar_cpf(cpf):
            # CPF válido, verificar existência de conta
            if Cliente.conta_exite(cpf):
                print("Encontrado")
                return True
            else:
                print("Não existe conta com esse CPF") 
        else:
            # CPF inválido
            print("CPF inválido! Deve conter apenas números e ter 11 dígitos.\n")
        return False
    
    @staticmethod
    def criar_conta():
        cpf = input("Digite o seu CPF (apenas números):\n>>> ")
        if Validador.validar_cpf(cpf):
            # CPF válido, verificar existência de conta
            if not Cliente.conta_exite(cpf):
                print("Vamos criar sua conta")
            else:
                print("Ja exite uma conta relacionada com esse cpf")
                return False
        else:
            # CPF inválido
            print("CPF inválido! Deve conter apenas números e ter 11 dígitos.\n")   
               
# Loop principal do programa
while True: 
    opcao = Menu.exibir_inicial()       # Mostra o menu inicial e captura a escolha do usuári
    
    if opcao == "L":
        if Login.logar_conta():
            opcao = Menu.exibir_principal()
            
            if opcao == "R":
                ...
            elif opcao == "D":
                ...            
            elif opcao == "S":
                ...            
            elif opcao == "V":
                ...            
            elif opcao == "E":
                ...            
            elif opcao == "Q":
                ...            
            else:
                print("Opção invalida")
        else:
            print("Não foi possivel realizar login")
                
    elif opcao == "C":
        if Login.criar_conta():
            ...
        else:
            print("Não foi possivel criar conta")
    else:
        print("Opção invalida")
 
    
                

        



# So iriar parecer apos login


LIMITES_DE_TRANSACOES_DIARIAS = 10
LIMITE_PARA_SAQUE = 500
transacoes_realizadas = 0
extrato = []
saldo = 0
usuarios = [[0]]
contas = [[0]]
cont_contas = 0
nome = ''
data_de_nascimento = ""
cpf = ''
endereco = ""

# Máscara para formatação de data e hora no padrão brasileiro
mascara_ptbr = '%d/%m/%Y %H:%M'
# Data e hora atual no fuso horário de São Paulo (GMT-3)
data_hora_atual = datetime.now(timezone(timedelta(hours=-3))).strftime(mascara_ptbr)



            
        






























