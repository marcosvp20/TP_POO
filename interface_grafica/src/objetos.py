from abc import ABC, abstractmethod
from planilhas import Planilha
class Objeto(ABC):
    def __init__(self, nome) -> None:
        self.nome = nome
        self.planilha = Planilha('objetos.xlsx')
        self.ligado = False
        
    def salvar(self,dados):
        self.planilha.salvar(dados)