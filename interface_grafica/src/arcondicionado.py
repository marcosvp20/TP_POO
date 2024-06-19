from interface_grafica.src.objetos import Objeto
from interface_grafica.src.planilha import Planilha

class ArCondicionado(Objeto):
    """
    Classe que representa um ar condicionado.

    Args:
        nome (str): O nome do ar condicionado.
        planilha (str): O caminho para a planilha onde os dados serão armazenados.

    Attributes:
        temperatura (int): A temperatura atual do ar condicionado.
        tipo (str): O tipo do ar condicionado.
        dados_ar (list): Uma lista com os dados do ar condicionado.

    Methods:
        mudar_temperatura: Altera a temperatura do ar condicionado.
        ligar: Liga o ar condicionado.
        desligar: Desliga o ar condicionado.
        salvar: Salva os dados do ar condicionado na planilha.
        temperatura_atual: Retorna a temperatura atual do ar condicionado.
        esta_ligado: Verifica se o ar condicionado está ligado.
        excluir: Exclui o ar condicionado da planilha.
    """

    def __init__(self, nome, planilha:Planilha) -> None:
        super().__init__(nome, planilha)
        self.__temperatura = 23
        self.tipo = 'A/C'
        self.dados_ar = [self.nome, self.tipo,self.__temperatura, self.ligado]

    def mudar_temperatura(self, temperatura) -> None:
        """
        Altera a temperatura do ar condicionado.

        Args:
            temperatura (int): A nova temperatura do ar condicionado.
        """
        self.dados_ar[2] = temperatura
        self.planilha.editar(self.dados_ar,2)
        
    def ligar(self) -> None:
        """
        Liga o ar condicionado.
        """
        self.dados_ar[3] = True
        self.planilha.editar(self.dados_ar,3)

    def desligar(self) -> None:
        """
        Desliga o ar condicionado.
        """
        self.dados_ar[3] = False
        self.planilha.editar(self.dados_ar,3)
    
    def salvar(self):
        """
        Salva os dados do ar condicionado na planilha.

        Returns:
            bool: True se os dados foram salvos com sucesso, False caso contrário.
        """
        if (self.planilha.retorna_quantidade('A/C') < 6):
            if not (self.planilha.verifica_se_objeto_existe(self.nome)):
                return super().salvar(self.dados_ar)
        return False
    
    def temperatura_atual(self) -> int:
        """
        Retorna a temperatura atual do ar condicionado.

        Returns:
            int: A temperatura atual do ar condicionado.
        """
        return self.planilha.retorna_valor(self.nome,3)
    
    def esta_ligado(self) -> bool:
        """
        Verifica se o ar condicionado está ligado.

        Returns:
            bool: True se o ar condicionado está ligado, False caso contrário.
        """
        return self.planilha.retorna_valor(self.nome,4)
    
    def excluir(self) -> bool:
        """
        Exclui o ar condicionado da planilha.

        Returns:
            bool: True se o ar condicionado foi excluído com sucesso, False caso contrário.
        """
        return self.planilha.excluir_dispositivo(self.nome)