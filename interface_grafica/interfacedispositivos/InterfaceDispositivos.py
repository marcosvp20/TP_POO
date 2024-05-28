import customtkinter as ctk
from PIL import Image, ImageTk
from interfacedispositivos.botao_disp import Botao
from interfacedispositivos.InterfaceNewDisp import InterfaceNewDisp
import os
from src.botao_dinamico import BotaoDinamico

class interfaceDispositivos:
    def __init__(self, janela) -> None:
        self.janela = janela
        
    def criaframe(self) -> None:
        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), 
                          size=(450,750))
        self.frame_dispositivos = ctk.CTkFrame(self.janela, 
                                                width=800, 
                                                height=500,
                                                fg_color= "transparent")
        self.frame_dispositivos.place(x=0, 
                                      y=0)
        
        label = ctk.CTkLabel(self.frame_dispositivos, 
                             width=450, 
                             height= 660, 
                             image=bg, 
                             text='')
        
        self.caixa_de_texto = ctk.CTkLabel(self.frame_dispositivos,
                                             text='Dispositivos: ',
                                             font=('League Spartan', 30),
                                             fg_color='white')
        self.caixa_de_texto.place(x = 10,
                                    y = 60)
        
        label.place(x = 0, 
                    y = 0)
        
    def botao_add (self) -> None:
        new_disp = InterfaceNewDisp(self.janela)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/plus.png'),size=(25,25))
        self.botao_adicionar = Botao(janela=self.frame_dispositivos, 
                                posx=42, 
                                posy=184, 
                                texto='Adicionar\nDispositivo', 
                                imagem=imagem,
                                comando = new_disp.executar)
        self.botao_adicionar.botao.place(x = 42, 
                                         y = 184)
        
    def executar(self) -> None:
        self.criaframe()
        #self.botao_add()
        self.frame_dispositivos.place(x = 0, 
                                      y = 0)
        new_disp = InterfaceNewDisp(self.janela)
        botao = BotaoDinamico(self.frame_dispositivos)
        