from abc import ABC, abstractmethod
import customtkinter as ctk

class IBotao(ABC):
    @abstractmethod
    def __init__(self, janela: ctk, posx: int, posy: int, texto: str, imagem=None, comando=None) -> None:
        pass
    
    @abstractmethod
    def botao_padrao(self) -> None:
        pass
    
    @abstractmethod
    def botao_menor(self, cor: str) -> None:
        pass
