from interfacedispositivos.InterfaceNewDisp import InterfaceNewDisp
from interfacedispositivos.b_dinamico_disp import BotaoDinamicoDisp
from src.frame import Frame
from src.planilha import Planilha

class interfaceDispositivos:
    def __init__(self, janela) -> None:
        """
        Classe responsável por criar a interface de dispositivos.
        """
        self.janela = janela
        self.planilha = Planilha('planilhas/objetos.xlsx')
        
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
        self.criaframe()
        InterfaceNewDisp(self.janela)
        # bd = BotaoDinamicoDisp(self.__frame_dispositivos, 'planilhas/objetos.xlsx')
        bd = BotaoDinamicoDisp(self.__frame_dispositivos, self.planilha)
        bd.insere_botao_add()
    
    def atualizar(self) -> None:
        """
        Atualiza a interface de dispositivos.
        """
        self.__frame_dispositivos.update()
        