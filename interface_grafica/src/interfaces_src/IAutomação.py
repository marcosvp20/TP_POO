from abc import ABC, abstractmethod

class IAutomacao(ABC):
    @abstractmethod
    def __init__(self, nome_auto: str) -> None:
        pass
    
    @abstractmethod
    def excluir_auto(self, coluna=None) -> bool:
        pass
    
    @abstractmethod
    def _excluir_temp(self) -> None:
        pass
    
    @abstractmethod
    def adicionar_auto(self) -> bool:
        pass
    
    @abstractmethod
    def retorna_nomes_auto(self) -> list:
        pass
    
    @abstractmethod
    def executar_automacao(self) -> None:
        pass
    
    @abstractmethod
    def verifica_alteracoes(self) -> None:
        pass
