import customtkinter as ctk
from src.frame import Frame
from interfacedispositivos.b_dinamico_disp import BotaoDinamicoDisp
from src.automacao import Automacao

class interfaceNewAuto:
    def __init__(self, janela) -> None:
        """
        Inicializa a classe interfaceNewAuto.
        """
        self.janela = janela
        pass
    
    def cria_frame(self) -> None:
        """
        Cria o frame para adicionar uma nova automação.
        """
        self.frame_new_auto = Frame(self.janela, 'Adicionar automação: ', '').frame
    
    def executar(self) -> None:
        """
        Executa a interface para adicionar uma nova automação.
        """
        self.cria_frame()
        auto = Automacao('')
        auto._Automacao__excluir_temp()
        auto.planilha_auto_temp = auto.planilha_disp
        BotaoDinamicoDisp(self.janela, 'automacoestemp.xlsx')
        
        
        