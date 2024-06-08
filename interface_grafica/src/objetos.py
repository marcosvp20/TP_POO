from abc import ABC, abstractmethod
from src.planilha import Planilha

class Objeto(ABC):
    def __init__(self, nome, planilha) -> None:
        self.nome = nome
        self.planilha = Planilha(planilha)
        self.ligado = False
        
    def salvar(self,dados) -> bool:
        self.planilha.salvar(dados)
        return True