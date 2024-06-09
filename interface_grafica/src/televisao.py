from src.objetos import Objeto

class Televisao (Objeto):
    """
    Classe que representa uma televisão.

    Attributes:
    - nome (str): O nome da televisão.
    - planilha (str): O nome da planilha onde os dados da televisão são armazenados.
    - canal (int): O número do canal atual da televisão.
    - volume (int): O nível de volume atual da televisão.
    - ligado (bool): Indica se a televisão está ligada ou desligada.
    - tipo (str): O tipo da televisão.
    - dados_tv (list): Lista com os dados da televisão.

    Methods:
    - __init__(self, nome:str, planilha:str): Construtor da classe Televisao.
    - ligar(self): Liga a televisão.
    - mudar_canal(self, novo_canal): Muda o canal da televisão.
    - mudar_volume(self, novo_volume): Muda o volume da televisão.
    - salvar(self): Salva os dados da televisão na planilha.
    - canal_atual(self): Retorna o número do canal atual da televisão.
    - volume_atual(self): Retorna o nível de volume atual da televisão.
    - esta_ligado(self): Retorna True se a televisão está ligada, False caso contrário.
    - excluir(self): Exclui a televisão da planilha.
    """

    def __init__ (self, nome:str, planilha:str) -> None:
        super().__init__(nome, planilha)
        self.canal = 1
        self.volume = 0
        self.ligado = False
        self.tipo = 'Televisor'
        self.dados_tv = [self.nome, self.tipo, self.canal, self.volume, self.ligado]

    def ligar (self) -> None:
        """
        Liga a televisão.

        Atualiza o status de ligado na planilha.
        """
        self.ligado = self.planilha.retorna_valor(self.nome, 5)
        if self.ligado == False:
            self.dados_tv [4] = True
        else:
            self.dados_tv[4] = False
        self.planilha.editar(self.dados_tv,4)

    def mudar_canal (self, novo_canal) -> None:
        """
        Muda o canal da televisão.

        Parâmetros:
        - novo_canal (int): O novo número do canal.
        """
        self.dados_tv[2] = novo_canal
        self.planilha.editar(self.dados_tv,2)

    def mudar_volume (self, novo_volume) -> None:
        """
        Muda o volume da televisão.

        Parâmetros:
        - novo_volume (int): O novo nível de volume.
        """
        if novo_volume > 100:
            self.dados_tv[3] = 100
            self.planilha.editar(self.dados_tv,3)
            return
        if novo_volume < 0:
            self.dados_tv[3] = 0
            self.planilha.editar(self.dados_tv,3)
            return
        self.dados_tv[3] = novo_volume
        self.planilha.editar(self.dados_tv,3)
    
    def salvar(self) -> bool:
        """
        Salva os dados da televisão na planilha.

        Retorna True se os dados foram salvos com sucesso, False caso contrário.
        """
        if self.planilha.retorna_quantidade('Televisor') < 6:
            if not (self.planilha.verifica_se_objeto_existe(self.nome)):
                return super().salvar(self.dados_tv)
        else:
            return False
    
    def canal_atual(self) -> int:
        """
        Retorna o número do canal atual da televisão.
        """
        return self.planilha.retorna_valor(self.nome, 3)
    
    def volume_atual(self) -> int:
        """
        Retorna o nível de volume atual da televisão.
        """
        return self.planilha.retorna_valor(self.nome, 4)
    
    def esta_ligado(self) -> bool:
        """
        Retorna True se a televisão está ligada, False caso contrário.
        """
        return self.planilha.retorna_valor(self.nome, 5)
    
    def excluir(self) -> bool:
        """
        Exclui a televisão da planilha.

        Retorna True se a televisão foi excluída com sucesso, False caso contrário.
        """
        return self.planilha.excluir_dispositivo(self.nome)
