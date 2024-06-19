from src.planilha import Planilha
from abc import ABC, abstractmethod

class Objeto(ABC):
    @abstractmethod
    def __init__(self, nome:str, planilha:Planilha) -> None:
        pass

    @abstractmethod
    def salvar(self, dados) -> bool:
        pass
