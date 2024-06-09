from tkinter import *
from PIL import Image
import customtkinter as ctk
from interfacedispositivos.botao_disp import Botao
from interfacedispositivos.InterfaceNameDisp import InterfaceNameDisp
from src.frame import Frame

class InterfaceNewDisp:
    """
    Classe responsável por criar a interface gráfica para adicionar novos dispositivos.
    """

    def __init__(self, janela) -> None:
        self.janela = janela
        
    def criaframe(self) -> None:
        """
        Cria o frame da interface para adicionar um novo dispositivo.
        """
        self.frame_new_disp = Frame(self.janela, 'Qual dispositivo deseja', 'adicionar?').frame
        
    def botao_ar (self) -> None:
        """
        Cria o botão para adicionar um ar condicionado.
        """
        new_ar = InterfaceNameDisp(self.janela, "A/C",self.frame_new_disp)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/arcondicionado.png'),size=(25,25))
        self.botao_adicionar = Botao(janela=self.frame_new_disp, 
                                 posx=135, 
                                 posy=184, 
                                 texto='Ar\nCondicionado', 
                                 imagem=imagem,
                                 comando = new_ar.executar)
        self.botao_adicionar.botao.place(x = 135, 
                                         y = 184)
        
    def botao_lampada (self) -> None:
        """
        Cria o botão para adicionar uma lâmpada.
        """
        new_lamp = InterfaceNameDisp(self.janela, "Lâmpada", self.frame_new_disp)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/lampada.png'),size=(25,25))
        self.botao_adicionar = Botao(janela=self.frame_new_disp, 
                                 posx=135, 
                                 posy=280, 
                                 texto='Lâmpada', 
                                 imagem=imagem,
                                 comando = new_lamp.executar)
        self.botao_adicionar.botao.place(x = 135, 
                                         y = 280)
        
    def botao_tv (self) -> None:
        """
        Cria o botão para adicionar uma TV.
        """
        new_tv = InterfaceNameDisp(self.janela, "Televisor",self.frame_new_disp)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/tv.png'),size=(25,25))
        self.botao_adicionar = Botao(janela=self.frame_new_disp, 
                                 posx=135, 
                                 posy=376,
                                 texto='TV', 
                                 imagem=imagem,
                                 comando = new_tv.executar)
        self.botao_adicionar.botao.place(x = 135, 
                                         y = 376)

    def executar(self) -> None:
        """
        Executa a interface gráfica.
        """
        self.criaframe()
        self.botao_ar()
        self.botao_lampada()
        self.botao_tv()