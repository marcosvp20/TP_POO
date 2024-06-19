from abc import abstractmethod, ABC
import customtkinter as ctk

class IMenuNewAuto(ABC):
    @abstractmethod
    def __init__(self, janela: ctk) -> None:
        pass
    
    @abstractmethod
    def cria_frame(self, mensagem1:str, mensagem2:str) -> None:
        pass
    
    @abstractmethod
    def insere_botoes(self) -> None:
        pass
    
    @abstractmethod
    def botaoProximo(self) -> None:
        pass
    
    @abstractmethod
    def atualiza_temp(self) -> None:
        pass
    
    @abstractmethod
    def executar(self) -> None:
        pass