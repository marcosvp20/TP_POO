from abc import ABC, abstractmethod

class InterfaceArCondicionado(ABC):
    """
    Interface para um ar condicionado.
    """
    @abstractmethod
    def mudar_temperatura(self, temperatura: int) -> None:
        pass
    
    @abstractmethod
    def ligar(self) -> None:
        pass
    
    @abstractmethod
    def desligar(self) -> None:
        pass
    
    @abstractmethod
    def salvar(self) -> bool:
        pass
    
    @abstractmethod
    def temperatura_atual(self) -> int:
        pass
    
    @abstractmethod
    def esta_ligado(self) -> bool:
        pass
    
    @abstractmethod
    def excluir(self) -> bool:
        pass
