from abc import ABC, abstractmethod

class InterfaceTelevisao(ABC):
    """
    Interface abstrata para representar uma televisão.
    """

    @abstractmethod
    def __init__(self, nome: str, planilha) -> None:
        """
        Inicializa a televisão com o nome e a planilha fornecidos.
        """
        pass

    @abstractmethod
    def ligar(self) -> None:
        """
        Liga a televisão.
        """
        pass

    @abstractmethod
    def mudar_canal(self, novo_canal: int) -> None:
        """
        Muda o canal da televisão.
        """
        pass

    @abstractmethod
    def mudar_volume(self, novo_volume: int) -> None:
        """
        Muda o volume da televisão.
        """
        pass

    @abstractmethod
    def salvar(self) -> bool:
        """
        Salva os dados da televisão na planilha.
        """
        pass

    @abstractmethod
    def canal_atual(self) -> int:
        """
        Retorna o número do canal atual da televisão.
        """
        pass

    @abstractmethod
    def volume_atual(self) -> int:
        """
        Retorna o nível de volume atual da televisão.
        """
        pass

    @abstractmethod
    def esta_ligado(self) -> bool:
        """
        Retorna True se a televisão está ligada, False caso contrário.
        """
        pass

    @abstractmethod
    def excluir(self) -> bool:
        """
        Exclui a televisão da planilha.
        """
        pass
