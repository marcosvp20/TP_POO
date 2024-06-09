import customtkinter as ctk

class Botao:
    """
    Classe que representa um botão personalizado em uma interface gráfica.

    Agumentos:
        janela (objeto): Objeto que representa a janela onde o botão será exibido.
        posx (int): Posição horizontal do botão na janela.
        posy (int): Posição vertical do botão na janela.
        texto (str): Texto exibido no botão.
        imagem (objeto): Imagem exibida no botão.
        comando (função, opcional): Função a ser executada quando o botão for clicado.

    Atributos:
        posx (int): Posição horizontal do botão na janela.
        posy (int): Posição vertical do botão na janela.
        botao (objeto): Objeto que representa o botão personalizado.

    """

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
        