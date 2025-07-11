from abc import ABC, abstractmethod
from datetime import datetime

contas = []
clientes = []
numero_conta = 1


class Cliente():
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        self._conta = conta
        transacao.registrar_transacao(self._conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    @property
    def contas(self):
        return self._contas


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf


class Conta():
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
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


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limites_saques = limite_saques

    def sacar(self, valor):
        numeros_de_saques_feitos = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
        )

        exedeu_limite = valor > self._limite
        exedeu_saques = numeros_de_saques_feitos >= self._limites_saques

        if exedeu_limite:
            print("Operação falhou!!!\nVc excedeu limite de saque")
        elif exedeu_saques:
            print("Operação falhou!!!\nVc excedeu limite de saques diários")
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\

            Agencia:\t{self._agencia}
            Conta corretente:\t{self._numero}
            Titular:\t{self.cliente.nome} 
            """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )


class interfaceTransacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar_transacao(self, conta):
        pass


class Saque(interfaceTransacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar_transacao(self, conta):
        sucesso_transacao = conta.sacar(self._valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(interfaceTransacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar_transacao(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Validador:
    @staticmethod
    def validar_cpf(cpf):
        if not cpf.isdigit() or len(cpf) != 11:
            return False
        else:
            return True


class Menu:
    @staticmethod
    def exibir_inicial():
        print("[L] Logar na conta")
        print("[Q] Sair")
        opcao = input(">>> ").upper()
        return opcao

    @staticmethod
    def exibir_principal():
        print("[R] Criar conta corrente")
        print("[D] Depositar")
        print("[S] Sacar")
        print("[V] Ver saldo")
        print("[E] extrato")
        print("[Q] Sair")
        opcao = input(">>> ").upper()
        return opcao


class Login():
    @staticmethod
    def logar_conta():
        cpf = input("Digite o CPF do proprietário da conta (apenas números):\n>>> ")
        if Validador.validar_cpf(cpf):
            print("Encontrado")
            return True
        else:
            print("CPF inválido! Deve conter apenas números e ter 11 dígitos.\n")
        return False


def criar_conta_corrente(cliente):
    global numero_conta
    conta = ContaCorrente(numero_conta, cliente)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    numero_conta += 1
    print(f"Conta corrente criada com sucesso! Número: {conta.numero}")
    return conta


def buscar_conta(cliente):
    if not cliente.contas:
        return None
    return cliente.contas[0]


def buscar_cliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None


def realizar_deposito(conta):
    try:
        valor = float(input("Digite o valor do depósito: R$ "))
        deposito = Deposito(valor)
        deposito.registrar_transacao(conta)
    except ValueError:
        print("Valor inválido!")


def realizar_saque(conta):
    try:
        valor = float(input("Digite o valor do saque: R$ "))
        saque = Saque(valor)
        saque.registrar_transacao(conta)
    except ValueError:
        print("Valor inválido!")


def exibir_extrato(conta):
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