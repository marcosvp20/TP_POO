from tkinter import *
from PIL import Image
import customtkinter as ctk
from interfacedispositivos.botao_disp import Botao
from interfacedispositivos.InterfaceNameDisp import InterfaceNameDisp

class InterfaceNewDisp:
    def __init__(self, janela) -> None:
        self.janela = janela
        
    def criaframe(self) -> None:
        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), 
                          size=(450,750))
        self.frame_new_disp = ctk.CTkFrame(self.janela, 
                                           width=800, 
                                           height=500,
                                           fg_color= "transparent")
        self.frame_new_disp.place(x=0, 
                                 y=0)
        
        label = ctk.CTkLabel(self.frame_new_disp, 
                             width=450, 
                             height= 660, 
                             image=bg, 
                             text='')
        
        label.place(x = 0, 
                    y = 0)
        
        self.caixa_de_texto1 = ctk.CTkLabel(self.frame_new_disp,
                                             text='Qual dispositivo deseja',
                                             font=('League Spartan', 30),
                                             fg_color='white')
        self.caixa_de_texto1.place(x = 10,
                                    y = 60)
        
        self.caixa_de_texto2 = ctk.CTkLabel(self.frame_new_disp,
                                             text='adicionar?:',
                                             font=('League Spartan', 30),
                                             fg_color='white')
        self.caixa_de_texto2.place(x = 10,
                                    y = 100)
        
    def botao_ar (self):
        new_ar = InterfaceNameDisp(self.janela)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/arcondicionado.png'),size=(25,25))
        self.botao_adicionar = Botao(janela=self.frame_new_disp, 
                                 posx=135, 
                                 posy=184, 
                                 texto='Ar\nCondicionado', 
                                 imagem=imagem,
                                 comando = new_ar.executar)
        self.botao_adicionar.botao.place(x = 135, 
                                         y = 184)
        
    def botao_lampada (self):
        new_lamp = InterfaceNameDisp(self.janela)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/lampada.png'),size=(25,25))
        self.botao_adicionar = Botao(janela=self.frame_new_disp, 
                                 posx=135, 
                                 posy=280, 
                                 texto='Lâmpada', 
                                 imagem=imagem,
                                 comando = new_lamp.executar)
        self.botao_adicionar.botao.place(x = 135, 
                                         y = 280)
        
    def botao_tv (self):
        new_tv = InterfaceNameDisp(self.janela)
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
        self.criaframe()
        self.frame_new_disp.place(x = 0, 
                                  y = 0)
        self.botao_ar()
        self.botao_lampada()
        self.botao_tv()