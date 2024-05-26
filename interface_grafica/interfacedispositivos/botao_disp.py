import customtkinter as ctk

class Botao:
    
    def __init__(self, janela, posx, posy, texto, imagem) -> None:
        self.posx = posx
        self.posy = posy
        self.botao = ctk.CTkButton(master=janela, 
                                   width= 187, 
                                   height=82, 
                                   text=texto, 
                                   font=('League Spartan bold',15),
                                   image= imagem, 
                                   compound='left', 
                                   fg_color='#d7ebf8', 
                                   text_color='black', 
                                   corner_radius=0)
        self.botao.place(x = self.posx, 
                         y = self.posy)
        