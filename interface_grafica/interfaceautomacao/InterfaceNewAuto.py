import customtkinter as ctk
from src.frame import Frame
from interfacedispositivos.b_dinamico_disp import BotaoDinamicoDisp
from src.automacao import Automacao

class interfaceNewAuto:
    def __init__(self, janela) -> None:
        self.janela = janela
        pass
    
    def cria_frame(self) -> None:
        self.frame_new_auto = Frame(self.janela, 'Adicionar automação: ', '').frame
    
    def executar(self) -> None:
        self.cria_frame()
        auto = Automacao('')
        auto._Automacao__excluir_temp()
        auto.planilha_auto_temp = auto.planilha_disp
        BotaoDinamicoDisp(self.janela, 'automacoestemp.xlsx')
        
        
        