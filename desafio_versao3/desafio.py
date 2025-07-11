# @staticmethod: O método não precisa acessar atributos da instância nem da classe.

# Importa classes base para herança abstrata e manipulação de datas e fuso horário
from abc import ABC, abstractmethod
from datetime import datetime

# Variáveis globais para armazenar dados
contas = []
clientes = []
numero_conta = 1


class Cliente():# Classe Cliente (abstração de um cliente do banco)
    def __init__(self, endereco):
        self._endereco = endereco        # Endereço do cliente (str)
        self._contas = []            # Lista de contas associadas ao cliente

    def realizar_transacao(self, conta, transacao):
        # Registra uma transação realizada
        self._conta = conta
        self._transacao = transacao
        
    def adicionar_cliente(self,conta):
        self._contas.append(conta)
        
    @property
    def contas(self):
        return self._contas
    

class PessoaFisica(Cliente): # Pessoa Física herda de Cliente e adiciona atributos específicos     
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf                          # CPF do cliente
        self._nome = nome                        # Nome do cliente
        self._data_nascimento = data_nascimento  # Data de nascimento     
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
        
        
class Conta():
    
    def __init__(self, numero,cliente): 
        # Inicializa os atributos da conta
        self._saldo = 0
        self._numero = numero # Número da conta (int)
        self._agencia = "0001" # Código da agência (str)
        self._cliente = cliente # Cliente da conta (Objeto da classe Cliente)
        self._historico = Historico() # Histórico da conta (instância da classe Historico)
    
    @classmethod 
    def nova_conta(cls, cliente,numero):
        return cls(cliente, numero)
        
    @property
    def saldo(self):
        return self._saldo        
    @property
    def numero(self):
        return self._numero        
    @property
    def agencia(self):
        return self._saldo        
    @property
    def cliente(self):
        return self._cliente        
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        
        saldo = self._saldo
        excedeu = valor > saldo
        
        if excedeu:
            print("Não conseguiu sacar - Saldo insuficiente")
            return False
        
        elif valor > 0:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("Operação falhou - Valor inválido")
            
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            return True
        
        else:
            print("Operação falhou - Valor inválido")
        return False


class ContaCorrente(Conta):# Classe ContaCorrente, herda de Conta
    def __init__(self, numero, cliente ,limite=500, limite_saques=3):
        # Reaproveita o construtor da classe base
        super().__init__(numero, cliente)
        self._limite = limite                    # Limite de crédito
        self._limites_saques = limite_saques     # Número de saques permitidos
        
    def sacar(self, valor):
        numeros_de_saques_feitos = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
            )
        
        exedeu_limite = valor > self._limite
        exedeu_saques = numeros_de_saques_feitos == self._limites_saques
        
        if exedeu_limite:
            print("Operação falhou!!!\nVc exedeu limite de saque")
        elif exedeu_saques:
            print("Operação falhou!!!\nVc exedeu limite de saques diarios")
        else: 
            return  super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agencia:\t{self._agencia}
            Conta corretente:\t{self._numero}
            Titular:\t{self.cliente.nome} 
            """
        

class Historico: # Classe de histórico de transações
    def __init__(self):
        self._transacoes = []  # Lista ou registro de transações
    
    @property
    def transacoes(self):
        return self._transacoes
    
    print(transacoes.__class__.__name__)
    
    def adicionar_transacao(self,transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )
       
       
class interfaceTransacao(ABC):# Interface abstrata para transações

    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar_transacao(self,conta):
        pass
    

class Saque(interfaceTransacao):# Classe de saque implementando a interface de transação
    def __init__(self, valor):
        self._valor = valor 
        
    @property
    def valor(self):
        return self._valor
    
    def registrar_transacao(self, conta):
        sucesso_transacao = conta.sacar(self._valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            

class Deposito(interfaceTransacao):# Classe de depósito implementando a interface de transação
    def __init__(self, valor):
        self._valor = valor 
        
    @property
    def valor(self):
        return self._valor
    
    def registrar_transacao(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Validador:# Validador de informações
  
    @staticmethod
    def validar_cpf(cpf):
        # Verifica se o CPF tem apenas números e 11 dígitos
        if not cpf.isdigit() or len(cpf) != 11:
            return False
        else:
            return True
      
        
class Menu:# Classe para exibir menus da aplicação
    @staticmethod 
    def exibir_inicial():
        # Exibe o menu inicial para o usuário
        print("[L] Logar na conta")       
        print("[Q] Sair")

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
    
 
class Login():# Classe para exibir o login
    @staticmethod
    def logar_conta():
        cpf = input("Digite o CPF do proprietário da conta (apenas números):\n>>> ")
        if Validador.validar_cpf(cpf):
            print("Encontrado")
            return True
        else:
            # CPF inválido
            print("CPF inválido! Deve conter apenas números e ter 11 dígitos.\n")
        return False
               

def criar_conta_corrente(cliente):
    """Cria uma nova conta corrente para um cliente"""
    global numero_conta
    
    conta = ContaCorrente(numero_conta, cliente)
    cliente.adicionar_cliente(conta)

    contas.append(conta)
    numero_conta += 1
    
    print(f"Conta corrente criada com sucesso! Número: {conta.numero}")
    return conta

def buscar_conta(cliente):
    """Busca uma conta do cliente"""
    if not cliente.contas:
        return None
    return cliente.contas[0]  # Retorna a primeira conta

def buscar_cliente(cpf):
    """Busca um cliente pelo CPF"""
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def realizar_deposito(conta):
    """Realiza um depósito na conta"""
    
    
    try:
        valor = float(input("Digite o valor do depósito: R$ "))
        deposito = Deposito(valor)
        deposito.registrar_transacao(conta)
    except ValueError:
        print("Valor inválido!")

def realizar_saque(conta):
    """Realiza um saque da conta"""
    try:
        valor = float(input("Digite o valor do saque: R$ "))
        saque = Saque(valor)
        saque.registrar_transacao(conta)
    except ValueError:
        print("Valor inválido!")

def exibir_extrato(conta):
    """Exibe o extrato da conta"""
    print("\n=== EXTRATO ===")
    print(f"Conta: {conta.numero}")
    print(f"Titular: {conta.cliente.nome}")
    print(f"Agência: {conta.agencia}")
    print("\nTransações:")
    
    if not conta.historico.transacoes:
        print("Nenhuma transação realizada.")
    else:
        for transacao in conta.historico.transacoes:
            print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
    
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("=" * 20)

               
while True: 
    opcao = Menu.exibir_inicial()
    
    if opcao == "L":
        cpf_ = input("Digite o CPF (apenas números): ")
        
        if not Validador.validar_cpf(cpf_):
            print("CPF inválido!")
            continue
        
        cliente = buscar_cliente(cpf_)
        
        if not cliente:
            # Cliente não existe, criar novo
            nome_ = input("Digite o nome: ")
            data_nascimento_ = input("Digite a data de nascimento (dd/mm/aaaa): ")
            endereco_ = input("Digite o endereço: ")
            
            cliente = PessoaFisica(endereco_, cpf_, nome_, data_nascimento_)
            clientes.append(cliente)
            
            print("Cliente criado com sucesso!\n")

        conta = buscar_conta(cliente)
        if not conta:
            print("Cliente não possui conta! Será criada uma conta um momento...")
            conta = criar_conta_corrente(cliente)
            
        print(f"\nLogin realizado com sucesso! Bem-vindo, {cliente.nome}!")

        while True:
            opcao = Menu.exibir_principal()
            
            if opcao == "R":
                criar_conta_corrente(cliente)
                
            elif opcao == "D":
                realizar_deposito(conta)
                
            elif opcao == "S":
                realizar_saque(conta)
                
            elif opcao == "V":
                print(f"Saldo atual: R$ {conta.saldo:.2f}")
                
            elif opcao == "E":
                exibir_extrato(conta)
                
            elif opcao == "Q":
                break
                
            else:
                print("Opção inválida")
                
    elif opcao == "Q":
        print("Obrigado por usar nosso sistema bancário!")
        break
    else:
        print("Opção inválida")
