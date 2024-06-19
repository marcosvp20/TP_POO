from abc import ABC, abstractmethod
import customtkinter as ctk

class IMenuExecutarAuto(ABC):
    @abstractmethod
    def __init__(self, janela: ctk, nome: str) -> None:
        pass

    @abstractmethod
    def criarframe(self) -> None:
        pass

    @abstractmethod
    def botaoAtivar(self) -> None:
        pass

    @abstractmethod
    def botaoExcluir(self) -> None:
        pass

    @abstractmethod
    def executar(self) -> None:
        pass
