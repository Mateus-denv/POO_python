# Importa recursos para criação de classes abstratas e métodos abstratos
from abc import ABC, abstractmethod

# Define a classe abstrata que servirá como contrato para os controles
class Controle_remoto(ABC):
    
    # Método abstrato: obriga qualquer subclasse a implementar o método 'ligar'
    @abstractmethod
    def ligar(self):
        pass
    
    # Método abstrato: obriga qualquer subclasse a implementar o método 'desligar'
    @abstractmethod
    def desligar(self):
        pass

# Classe concreta que herda da classe abstrata Controle_remoto
# e implementa os métodos obrigatórios definidos no contrato
class Controletv(Controle_remoto):
    
    # Implementação concreta do método 'ligar'
    def ligar(self):
        print('Ligando tv')
        
    # Implementação concreta do método 'desligar'
    def desligar(self):
        print("Desligando tv")
    
    # Propriedade adicional específica da classe Controletv
    @property
    def marca(self):
        return "LG"

# Outra classe concreta que também herda da classe abstrata Controle_remoto
class ControleArcondionado(Controle_remoto):
    
    # Implementação concreta do método 'ligar'
    def ligar(self):
        print('Ligando ar')
        
    # Implementação concreta do método 'desligar'
    def desligar(self):
        print("Desligando ar")
    
    # Propriedade adicional específica da classe ControleArcondionado
    @property
    def marca(self):
        return "TCL"

# Instanciando e utilizando a classe Controletv
controle = Controletv()
controle.ligar()          
controle.desligar()       

# Reutilizando a variável 'controle' para uma instância de ControleArcondionado
controle = ControleArcondionado()
controle.ligar()          
controle.desligar()       
print(controle.marca)     
