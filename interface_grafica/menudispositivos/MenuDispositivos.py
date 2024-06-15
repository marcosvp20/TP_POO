from menudispositivos.b_dinamico_disp import BotaoDinamicoDisp
from src.frame import Frame
from src.planilha import Planilha

class MenuDispositivos:
    """
    Classe responsável por criar a interface de dispositivos.
    """
    def __init__(self, janela) -> None:
        """
        Inicializa o menu de dispositivos.

        Argumentos:
            janela(ctk): Janela referência à inicialização do menu.
        """    
        self.janela = janela
        
    def criaframe(self) -> None:
        """
        Cria o frame da interface de dispositivos.
        """
        self.__frame = Frame(self.janela, 'Dispositivos: ', '')
        self.__frame_dispositivos = self.__frame.retorna_frame()
        
    def executar(self) -> None:
        """
        Executa a interface de dispositivos.
        """
        self.planilha = Planilha('planilhas/objetos.xlsx')
        self.criaframe()
        bd = BotaoDinamicoDisp(self.__frame_dispositivos, self.planilha)
        bd.insere_botao_add()
    
    def atualizar(self) -> None:
        """
        Atualiza a interface de dispositivos.
        """
        self.__frame_dispositivos.update()
        