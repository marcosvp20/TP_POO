from interface_grafica.src.interfaces_src.IObjeto import IObjeto
from interface_grafica.src.planilha import Planilha

class Objeto(IObjeto):
    def __init__(self, nome:str, planilha:Planilha) -> None:
        """
        Inicializa um objeto com um nome e uma planilha.

        Args:
            nome (str): O nome do objeto.
            planilha (Planilha): A instância da classe Planilha associada ao objeto.
        """
        self.nome = nome
        self.planilha = planilha
        self.ligado = False
        
    def salvar(self,dados:list) -> bool:
        """
        Salva os dados na planilha associada ao objeto.

        Args:
            dados: Os dados a serem salvos na planilha.

        Returns:
            bool: True se os dados foram salvos com sucesso, False caso contrário.
        """
        self.planilha.salvar(dados)
        return True