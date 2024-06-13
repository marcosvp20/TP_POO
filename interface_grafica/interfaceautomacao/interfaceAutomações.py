import customtkinter as ctk
from PIL import Image
from interfaceautomacao.botao_auto import Botao
from interfaceautomacao.b_dinamico_auto import BotaoDinamicoAuto
from src.frame import Frame

class interfaceAutomacoes:
    def __init__(self, janela) -> None:
        """
        Classe responsável por criar a interface gráfica para automações.
        """
        self.janela = janela
    
    def criarframe(self) -> None:
        """
        Cria o frame para exibir as automações.
        """
        self.__frame = Frame(self.janela, 'Automações: ', '')
        self.__frame_automacoes = self.__frame.retorna_frame()
   
    def executar(self) -> None:
        """
        Executa a interface gráfica de automações.
        """
        self.criarframe()
        bd = BotaoDinamicoAuto(self.__frame_automacoes)
        bd.insere_botao_add()