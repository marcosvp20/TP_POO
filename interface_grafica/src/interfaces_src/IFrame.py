from abc import ABC, abstractmethod
import customtkinter as ctk

class IFrame(ABC):
    @abstractmethod
    def __init__(self, janela: ctk, texto1: str, texto2: str) -> None:
        pass

    @abstractmethod
    def retorna_frame(self):
        pass

    @abstractmethod
    def mensagem(self, mensagem: str):
        pass

    @abstractmethod
    def destroy(self):
        pass
