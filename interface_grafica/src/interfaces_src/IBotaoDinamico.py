from abc import ABC, abstractmethod
import customtkinter as ctk
from PIL import Image

class IBotaoDinamico(ABC):

    @abstractmethod
    def __init__(self, janela: ctk) -> None:
        pass

    @abstractmethod
    def configura_botao(self, posx: int, posy: int, texto: str, imagem: Image, comando) -> None:
        pass

    @abstractmethod
    def importar_posicoes(self) -> None:
        pass

    @abstractmethod
    def importa_nomes(self) -> None:
        pass