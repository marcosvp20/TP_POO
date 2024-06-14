from abc import ABC, abstractmethod
import customtkinter as ctk

class InterfaceJanelaPrincipal(ABC):
    @abstractmethod
    def __init__(self) -> None:
        """
        Inicializa a janela principal da aplicação.
        """
        pass

    @abstractmethod
    def configurar_janela(self) -> None:
        """
        Configura a aparência da janela, define o título e o tamanho.
        """
        pass

    @abstractmethod
    def criar_imagem_fundo(self) -> None:
        """
        Cria um rótulo com a imagem de fundo.
        """
        pass

    @abstractmethod
    def criar_frame_inferior(self) -> None:
        """
        Cria o frame inferior.
        """
        pass

    @abstractmethod
    def executar(self) -> None:
        """
        Executa o loop principal da janela.
        """
        pass
