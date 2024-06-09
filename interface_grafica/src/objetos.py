from abc import ABC, abstractmethod
from src.planilha import Planilha

class Objeto(ABC):
    def __init__(self, nome, planilha) -> None:
        """
        Inicializa um objeto com um nome e uma planilha.

        Args:
            nome (str): O nome do objeto.
            planilha (str): O caminho para a planilha associada ao objeto.
        """
        self.nome = nome
        self.planilha = Planilha(planilha)
        self.ligado = False
        
    def salvar(self,dados) -> bool:
        """
        Salva os dados na planilha associada ao objeto.

        Args:
            dados: Os dados a serem salvos na planilha.

        Returns:
            bool: True se os dados foram salvos com sucesso, False caso contrário.
        """
        self.planilha.salvar(dados)
        return True