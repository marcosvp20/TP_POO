from abc import ABC, abstractmethod
import customtkinter as ctk

class IMenuDispositivos(ABC):
    @abstractmethod
    def __init__(self, janela: ctk) -> None:
        pass

    @abstractmethod
    def criaframe(self) -> None:
        pass

    @abstractmethod
    def executar(self) -> None:
        pass

    @abstractmethod
    def atualizar(self) -> None:
        pass
