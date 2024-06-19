from abc import ABC, abstractmethod
import customtkinter as ctk
from src.planilha import Planilha

class IMenuNewDisp(ABC):
    @abstractmethod
    def __init__(self, janela: ctk, planilha: Planilha) -> None:
        pass
    
    @abstractmethod
    def criaframe(self) -> None:
        pass
    
    @abstractmethod
    def botao_ar(self) -> None:
        pass
    
    @abstractmethod
    def botao_lampada(self) -> None:
        pass
    
    @abstractmethod
    def botao_tv(self) -> None:
        pass
    
    @abstractmethod
    def executar(self) -> None:
        pass
