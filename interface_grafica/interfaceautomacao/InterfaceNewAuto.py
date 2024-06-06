import customtkinter as ctk
from PIL import Image

class interfaceNewAuto:
    def __init__(self, janela) -> None:
        self.janela = janela
        pass
    
    def cria_frame(self) -> None:

        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), 
                            size=(450,750))
        self.frame_new_auto = ctk.CTkFrame(self.janela, 
                                            width=800, 
                                            height=500,
                                            fg_color= "transparent")
        self.frame_new_auto.place(x=0, 
                                    y=0)
        label = ctk.CTkLabel(self.frame_new_auto, 
                             width=450, 
                             height= 660, 
                             image=bg, 
                             text='')
        
        label.place(x = 0, 
                    y = 0)
        
        self.caixa_de_texto1 = ctk.CTkLabel(self.frame_new_auto,
                                             text='Adicionar automação:',
                                             font=('League Spartan', 30),
                                             fg_color='white')
        self.caixa_de_texto1.place(x = 10,
                                    y = 60)
    
    def executar(self) -> None:
        self.cria_frame()
        
        