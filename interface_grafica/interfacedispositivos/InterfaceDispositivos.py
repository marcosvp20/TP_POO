import customtkinter as ctk
from PIL import Image
from interfacedispositivos.botao_disp import Botao
from interfacedispositivos.InterfaceNewDisp import InterfaceNewDisp
import os
from src.botao_dinamico import BotaoDinamico

class interfaceDispositivos:
    def __init__(self, janela) -> None:
        """
        Classe responsável por criar a interface de dispositivos.
        """
        self.janela = janela
        
    def criaframe(self) -> None:
        """
        Cria o frame da interface de dispositivos.
        """
        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), 
                          size=(450,750))
        self.frame_dispositivos = ctk.CTkFrame(self.janela, 
                                                width=450, 
                                                height=660,
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
        
    def executar(self) -> None:
        """
        Executa a interface de dispositivos.
        """
        self.criaframe()
        new_disp = InterfaceNewDisp(self.janela)
        botao = BotaoDinamico(self.frame_dispositivos)
    
    def atualizar(self) -> None:
        """
        Atualiza a interface de dispositivos.
        """
        self.frame_dispositivos.update()
        