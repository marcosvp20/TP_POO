from abc import ABC, abstractmethod
from planilha import Planilha

class Objeto(ABC):
    def __init__(self, nome) -> None:
        self.nome = nome
        self.planilha = Planilha('objetos.xlsx')
        
    @abstractmethod
    def salvar(self):
        pass