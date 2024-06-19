from abc import ABC, abstractmethod

class Planilha(ABC):
    @abstractmethod
    def __init__(self, nome_planilha:str) -> None:
        pass

    @abstractmethod
    def salvar(self, dados:list) -> bool:
        pass

    @abstractmethod
    def editar(self, dados:list, coluna:int) -> None:
        pass

    @abstractmethod
    def verifica_se_objeto_existe(self, nome: str) -> bool:
        pass

    @abstractmethod
    def retorna_valor(self, nome:str, coluna:int) -> str:
        pass

    @abstractmethod
    def exclui_linha_vazia(self) -> None:
        pass

    @abstractmethod
    def retorna_quantidade(self, tipo:str) -> int:
        pass

    @abstractmethod
    def verifica_se_esta_vazio(self) -> bool:
        pass

    @abstractmethod
    def retorna_quantidade_linhas(self) -> int:
        pass

    @abstractmethod
    def retorna_coluna(self, letra_coluna:int) -> list:
        pass

    @abstractmethod
    def retorna_linha(self, numero_linha:int) -> list:
        pass

    @abstractmethod
    def limpar_planilha(self) -> None:
        pass

    @abstractmethod
    def excluir_linha(self, nome:str, coluna:int) -> bool:
        pass

    @abstractmethod
    def selecionar(self, objeto_id:str) -> None:
        pass
