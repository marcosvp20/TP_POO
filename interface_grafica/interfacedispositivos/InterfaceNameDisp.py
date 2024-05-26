from tkinter import *
from PIL import Image
import customtkinter as ctk
from interfacedispositivos.botao_disp import Botao

class InterfaceNameDisp:
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
                                             text='Qual dispositivo será o nome',
                                             font=('League Spartan', 30),
                                             fg_color='white')
        self.caixa_de_texto1.place(x = 10,
                                    y = 60)
        
        self.caixa_de_texto2 = ctk.CTkLabel(self.frame_new_disp,
                                             text='do dispositivo?',
                                             font=('League Spartan', 30),
                                             fg_color='white')
        self.caixa_de_texto2.place(x = 10,
                                    y = 100)
        
        self.txtbox_name_disp = ctk.CTkEntry(self.frame_new_disp, 
                                 width=180, 
                                 font=('League Spartan', 20),
                                 placeholder_text="Nome do dispositivo",
                                 placeholder_text_color="gray")
        self.txtbox_name_disp.place(x=135,   
                            y=200)
        
    def botao_confirmar (self):
        imagem = ctk.CTkImage(light_image= Image.open('imagens/plus.png'),size=(25,25))
        self.botao_adicionar = Botao(janela=self.frame_new_disp, 
                                 posx=135, 
                                 posy=250, 
                                 texto='Confirmar', 
                                 imagem=imagem)
        self.botao_adicionar.botao.place(x = 135, 
                                         y = 250)
        
    def executar(self) -> None:
        self.criaframe()
        self.botao_confirmar()