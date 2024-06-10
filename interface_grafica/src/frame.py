import customtkinter as ctk
from PIL import Image

class Frame:
    def __init__(self, janela, texto1, texto2='') -> None:
        """
        Classe que representa um frame na interface gráfica.

        Args:
            janela (objeto): Objeto da janela onde o frame será exibido.
            texto1 (str): Texto a ser exibido na primeira caixa de texto.
            texto2 (str): Texto a ser exibido na segunda caixa de texto.

        Attributes:
            frame (objeto): Objeto do frame.
            caixa_de_texto1 (objeto): Objeto da primeira caixa de texto.
            caixa_de_texto2 (objeto): Objeto da segunda caixa de texto (opcional).
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