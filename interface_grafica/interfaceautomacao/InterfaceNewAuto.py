import customtkinter as ctk
from PIL import Image
from src.frame import Frame


class interfaceNewAuto:
    def __init__(self, janela) -> None:
        self.janela = janela
        pass
    
    def cria_frame(self) -> None:
        self.frame_new_auto = Frame(self.janela, 'Adicionar automação: ', '').frame
    
    def executar(self) -> None:
        self.cria_frame()
        
        