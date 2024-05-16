from abc import ABC, abstractmethod
from planilha import Planilha

class Objeto(ABC):
    def __init__(self, nome) -> None:
        self.nome = nome
        self.planilha = Planilha('objetos.xlsx')
        self.ligado = False
        
    @abstractmethod
    def salvar(self):
        pass
    @abstractmethod
    def ligar(self):
        pass