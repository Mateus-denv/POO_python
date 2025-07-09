class Conta():
    def __init__(self, agencia, saldo=0):
        self._saldo = saldo
        self.agencia = agencia
        
    def sacar(self,sacar):
        #...
        self._saldo -= sacar
    
    def depositar(self, deposita):
        self._saldo += deposita
        
    def mostrar_saldo(self):
        return self._saldo

conta = Conta("0-001",1000)
conta.depositar(deposita=20)
conta.sacar(sacar=200)
print(conta.agencia)
print(conta.mostrar_saldo())
