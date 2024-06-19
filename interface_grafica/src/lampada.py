from interface_grafica.src.objetos import Objeto
from interface_grafica.src.planilha import Planilha

class Lampada(Objeto):
    def __init__(self, nome, planilha:Planilha) -> None:
        """
        Inicializa uma instância da classe Lampada.

        Args:
            nome (str): O nome da lâmpada.
            planilha (str): O caminho para a planilha onde os dados serão armazenados.
        """
        super().__init__(nome, planilha)
        self.brilho = 0
        self.tipo = 'Lâmpada'
        self.dados_lampada = [self.nome, self.tipo, self.brilho, self.ligado]
        
    def ligar(self) -> None:
        """
        Liga a lâmpada.
        """
        self.ligado = self.planilha.retorna_valor(self.nome, 4)
        if self.ligado == False:
            self.dados_lampada[3] = True
        else:
            self.dados_lampada[3] = False
        self.planilha.editar(self.dados_lampada,3)
        
    def mudar_brilho(self, porcentagem:int) -> None:
        """
        Muda o brilho da lâmpada para a porcentagem especificada.

        Args:
            porcentagem (int): A porcentagem de brilho desejada.
        """
        self.dados_lampada[2] = porcentagem
        self.planilha.editar(self.dados_lampada,2)
    
    def brilho_atual(self) -> int:
        """
        Retorna o brilho atual da lâmpada.

        Returns:
            int: O brilho atual da lâmpada.
        """
        return self.planilha.retorna_valor(self.nome, 3)
    
    def esta_ligado(self) -> bool:
        """
        Verifica se a lâmpada está ligada.

        Returns:
            bool: True se a lâmpada está ligada, False caso contrário.
        """
        return self.planilha.retorna_valor(self.nome, 4)
    
    def excluir(self) -> bool:
        """
        Exclui a lâmpada.

        Returns:
            bool: True se a lâmpada foi excluída com sucesso, False caso contrário.
        """
        return self.planilha.excluir_dispositivo(self.nome)

    def salvar(self) -> bool:
        """
        Salva a lâmpada na planilha.

        Returns:
            bool: True se a lâmpada foi salva com sucesso, False caso contrário.
        """
        if self.planilha.retorna_quantidade('Lâmpada') < 6:
            if not (self.planilha.verifica_se_objeto_existe(self.nome)):
                return super().salvar(self.dados_lampada)
        else:
            return False
        
