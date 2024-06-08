import customtkinter as ctk
from PIL import Image

class Frame:
    def __init__(self, janela, texto1, texto2) -> None:
        """
        Cria um frame com jnaela e textos passados como parâmetros: um texto por linha.
        """
        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), 
                          size=(450,750))
        self.frame = ctk.CTkFrame(janela, 
                                  width=450, 
                                  height=660,
                                  fg_color= "transparent")
        self.frame.place(x=0, 
                         y=0)
        
        label = ctk.CTkLabel(self.frame, 
                             width=450, 
                             height= 660, 
                             image=bg, 
                             text='')
        
        self.caixa_de_texto1 = ctk.CTkLabel(self.frame,
                                           text=texto1,
                                           font=('League Spartan', 30),
                                           fg_color='white')
        
        self.caixa_de_texto1.place(x = 10,
                                  y = 60)
        
        label.place(x = 0, 
                    y = 0)
        
        if texto2 != '':
            self.caixa_de_texto2 = ctk.CTkLabel(self.frame,
                                             text=texto2,
                                             font=('League Spartan', 30),
                                             fg_color='white')
            self.caixa_de_texto2.place(x = 10,
                                       y = 100)