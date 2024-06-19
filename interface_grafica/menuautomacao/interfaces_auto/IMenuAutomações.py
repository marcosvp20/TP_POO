from abc import ABC, abstractmethod
import customtkinter as ctk

class IMenuAutomacoes(ABC):
    @abstractmethod
    def __init__(self, janela: ctk) -> None:
        pass

    @abstractmethod
    def criarframe(self) -> None:
        pass

    @abstractmethod
    def executar(self) -> None:
        pass
