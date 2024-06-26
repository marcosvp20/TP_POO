from abc import ABC, abstractmethod
import customtkinter as ctk
from interface_grafica.src.planilha import Planilha

class IMenuTV(ABC):
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
    def ligar_desligar(self) -> None:
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
    def botoes_mudar_canal(self) -> None:
        pass
    
    @abstractmethod
    def click_botao_mais(self) -> None:
        pass
    
    @abstractmethod
    def click_botao_menos(self) -> None:
        pass
    
    @abstractmethod
    def alterar_canal(self, canal: int) -> None:
        pass
    
    @abstractmethod
    def excluir(self) -> None:
        pass
    
    @abstractmethod
    def mensagem(self, texto: str) -> None:
        pass
    
    @abstractmethod
    def atualiza_valor(self, value) -> None:
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
