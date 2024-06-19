from interface_grafica.menudispositivos.interfaces_disp.IMenuNewDisp import IMenuNewDisp
from tkinter import *
from PIL import Image
import customtkinter as ctk
from interface_grafica.menudispositivos.MenuNameDisp import MenuNameDisp
from interface_grafica.src.frame import Frame
from interface_grafica.src.botao import Botao
from interface_grafica.src.planilha import Planilha

class MenuNewDisp(IMenuNewDisp):
    """
    Classe responsável por criar a interface gráfica para adicionar novos dispositivos.
    """
    def __init__(self, janela, planilha:Planilha) -> None:
        """
        Inicializa o menu de definição de um novo dispositivo.

        Argumentos:
            janela(ctk): Janela onde o frame da interface será fixado.
            planilha(Planilha): Planilha que contém os dados a serem utilizados.
        """
        self.janela = janela
        self.planilha = planilha
        
    def criaframe(self) -> None:
        """
        Cria o frame da interface para adicionar um novo dispositivo.
        """
        self.__frame = Frame(self.janela, 'Qual dispositivo deseja', 'adicionar?')
        self.__frame_new_disp = self.__frame.retorna_frame()
        
    def botao_ar (self) -> None:
        """
        Cria o botão para adicionar um ar condicionado.
        """
        new_ar = MenuNameDisp(self.janela, "A/C", self.planilha)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/arcondicionado.png'),size=(25,25))
        self.botaoAr = Botao(janela=self.__frame_new_disp, 
                                 posx=135, 
                                 posy=184, 
                                 texto='Ar\nCondicionado', 
                                 imagem=imagem,
                                 comando = new_ar.executar)
        self.botaoAr.botao_padrao()
        
    def botao_lampada (self) -> None:
        """
        Cria o botão para adicionar uma lâmpada.
        """
        new_lamp = MenuNameDisp(self.janela, "Lâmpada", self.planilha)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/lampada.png'),size=(25,25))
        self.botaoLamp = Botao(janela=self.__frame_new_disp, 
                                 posx=135, 
                                 posy=280, 
                                 texto='Lâmpada', 
                                 imagem=imagem,
                                 comando = new_lamp.executar)
        self.botaoLamp.botao_padrao()
        
    def botao_tv (self) -> None:
        """
        Cria o botão para adicionar uma TV.
        """
        new_tv = MenuNameDisp(self.janela, "Televisor", self.planilha)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/tv.png'),size=(25,25))
        self.botaoTv = Botao(janela=self.__frame_new_disp, 
                                 posx=135, 
                                 posy=376,
                                 texto='TV', 
                                 imagem=imagem,
                                 comando = new_tv.executar)
        self.botaoTv.botao_padrao()

    def executar(self) -> None:
        """
        Executa a interface gráfica.
        """
        self.criaframe()
        self.botao_ar()
        self.botao_lampada()
        self.botao_tv()