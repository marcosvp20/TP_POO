import customtkinter as ctk
from PIL import Image
from interfaceautomacao.botao_auto import Botao
from interfaceautomacao.b_dinamico_auto import BotaoDinamico
from src.frame import Frame

class interfaceAutomacoes:
    def __init__(self, janela) -> None:
        self.janela = janela
    
    def criarframe(self) -> None:
        self.frame_automacoes = Frame(self.janela, 'Automações: ', '').frame
   
    def executar(self) -> None:
        self.criarframe()
        BotaoDinamico(self.frame_automacoes)