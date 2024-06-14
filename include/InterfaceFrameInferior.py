from abc import ABC, abstractmethod
import customtkinter as ctk

class InterfaceFrameInferior(ABC):
    def __init__(self, janela) -> None:
        """
        Inicializa o frame inferior.
        """
        self.janela = janela

    @abstractmethod
    def criaframe(self) -> None:
        """
        Método abstrato para criar o frame inferior na janela principal.
        """
        pass

    @abstractmethod
    def botaodispositivos(self) -> None:
        """
        Método abstrato para criar o botão de Dispositivos no frame inferior.
        """
        pass

    @abstractmethod
    def botaoautomacao(self) -> None:
        """
        Método abstrato para criar o botão de Automações no frame inferior.
        """
        pass

    @abstractmethod
    def executar(self) -> None:
        """
        Método abstrato para executar a criação do frame inferior e dos botões de Dispositivos e Automações.
        """
        pass
