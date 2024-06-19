from abc import ABC, abstractmethod
import customtkinter as ctk
from src.planilha import Planilha

class IMenuNameDisp(ABC):
    @abstractmethod
    def __init__(self, janela: ctk, tipo: str, planilha: Planilha) -> None:
        pass

    @abstractmethod
    def criaframe(self) -> None:
        pass

    @abstractmethod
    def botao_confirmar(self) -> None:
        pass

    @abstractmethod
    def adicionar(self) -> None:
        pass

    @abstractmethod
    def mensagem_confirmacao(self, mensagem:str) -> None:
        pass

    @abstractmethod
    def apagar_mensagem_confirmacao(self) -> None:
        pass

    @abstractmethod
    def parar_execucao(self) -> None:
        pass

    @abstractmethod
    def executar(self) -> None:
        pass
