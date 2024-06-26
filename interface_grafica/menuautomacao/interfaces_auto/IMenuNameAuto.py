from abc import ABC, abstractmethod
import customtkinter as ctk
from interface_grafica.src.automacao import Automacao

class IMenuNameAuto(ABC):
    @abstractmethod
    def __init__(self, janela: ctk, auto: Automacao) -> None:
        pass

    @abstractmethod
    def criaframe(self) -> None:
        pass

    @abstractmethod
    def criar_entry(self) -> None:
        pass

    @abstractmethod
    def botao_confirmar(self) -> None:
        pass

    @abstractmethod
    def executar(self) -> None:
        pass
