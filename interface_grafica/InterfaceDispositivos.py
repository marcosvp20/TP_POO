import customtkinter as ctk
from PIL import Image, ImageTk
import os

class interfaceDispositivos:
    def __init__(self, janela) -> None:
        self.janela = janela
        
    def criaframe(self) -> None:
        self.frame_dispositivos = ctk.CTkFrame(self.janela, 
                                                width=800, 
                                                height=500,
                                                fg_color= "white")
        self.frame_dispositivos.place(x=0, y=0)
        self.botao_ar = ctk.CTkButton(self.frame_dispositivos, 
                                      text="Ar-Condicionados", 
                                      command=self.botao_ar)
        
    def botao_ar ():
        pass
        
    def executar(self) -> None:
        self.criaframe()
        self.frame_dispositivos.place(x = 0, 
                                      y = 0)
        