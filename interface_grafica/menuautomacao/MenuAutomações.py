import customtkinter as ctk
from interface_grafica.menuautomacao.b_dinamico_auto import BotaoDinamicoAuto
from interface_grafica.src.frame import Frame

class MenuAutomacoes:
    """
    Classe responsável por criar a interface gráfica para automações.
    """
    def __init__(self, janela:ctk) -> None:
        """
        Inicializa o menu das automações.
        
        Argumentos:
            janela(ctk): a janela na qual será fixado frame das automações.
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