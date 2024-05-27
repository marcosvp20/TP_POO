from abc import ABC, abstractmethod
from src.planilha import Planilha

class Objeto(ABC):
    def __init__(self, nome) -> None:
        self.nome = nome
        self.planilha = Planilha('objetos.xlsx')
        self.ligado = False
        
    def salvar(self,dados) -> bool:
        self.planilha.salvar(dados)
        return True