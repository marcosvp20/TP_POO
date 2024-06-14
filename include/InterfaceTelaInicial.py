from abc import ABC, abstractmethod
import customtkinter as ctk

class InterfaceTelaInicial(ABC):
    def __init__(self, janela: ctk) -> None:
        """
        Classe abstrata responsável por criar a estrutura básica da tela.
        """
        self.janela = janela

    @abstractmethod
    def cria_frame(self) -> None:
        """
        Método abstrato para criar o frame da tela.
        """
        pass

    @abstractmethod
    def cria_texto(self, texto: str) -> None:
        """
        Método abstrato para criar o texto na tela.
        """
        pass

    @abstractmethod
    def importar_hora(self) -> None:
        """
        Método abstrato para importar a hora atual do sistema.
        """
        pass

    @abstractmethod
    def executar(self) -> None:
        """
        Método abstrato para executar a criação da tela.
        """
        pass
