from abc import ABC, abstractmethod

class InterfaceLampada(ABC):
    """
    Interface abstrata para representar uma lâmpada.
    """

    @abstractmethod
    def __init__(self, nome: str, planilha) -> None:
        """
        Inicializa a lâmpada com o nome e a planilha fornecidos.
        """
        pass

    @abstractmethod
    def ligar(self) -> None:
        """
        Liga a lâmpada.
        """
        pass

    @abstractmethod
    def mudar_brilho(self, porcentagem: int) -> None:
        """
        Muda o brilho da lâmpada para a porcentagem especificada.
        """
        pass

    @abstractmethod
    def brilho_atual(self) -> int:
        """
        Retorna o brilho atual da lâmpada.
        """
        pass

    @abstractmethod
    def esta_ligado(self) -> bool:
        """
        Verifica se a lâmpada está ligada.
        """
        pass

    @abstractmethod
    def excluir(self) -> bool:
        """
        Exclui a lâmpada.
        """
        pass

    @abstractmethod
    def salvar(self) -> bool:
        """
        Salva a lâmpada na planilha.
        """
        pass
