from abc import ABC, abstractmethod
import customtkinter as ctk
from src.planilha import Planilha

class IMenuAC(ABC):
    @abstractmethod
    def __init__(self, janela: ctk, nome: str, planilha: Planilha) -> None:
        pass

    @abstractmethod
    def criaframe(self) -> None:
        pass

    @abstractmethod
    def switch(self) -> None:
        pass
    
    @abstractmethod
    def slider(self) -> None:
        pass

    @abstractmethod
    def botaoExcluir(self) -> None:
        pass

    @abstractmethod
    def botaoVoltar(self) -> None:
        pass

    @abstractmethod
    def ligar_desligar(self) -> None:
        pass

    @abstractmethod
    def atualiza_valor(self, value) -> None:
        pass

    @abstractmethod
    def excluir(self) -> None:
        pass

    @abstractmethod
    def mensagem(self, mensagem: str) -> None:
        pass

    @abstractmethod
    def botaoConfirmar(self) -> None:
        pass

    @abstractmethod
    def confirmar(self) -> None:
        pass

    @abstractmethod
    def executar(self) -> None:
        pass
