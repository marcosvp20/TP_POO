from interface_grafica.src.interfaces_src.IBotao import IBotao
import customtkinter as ctk

class Botao(IBotao):
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

    def __init__(self, janela:ctk, posx:int, posy:int, texto:str, imagem = None, comando = None) -> None:

        """
        Inicializa um botão personalizado na interface gráfica.

        Args:
            janela (ctk): Objeto que representa a janela onde o botão será exibido.
            posx (int): Posição horizontal do botão na janela.
            posy (int): Posição vertical do botão na janela.
            texto (str): Texto exibido no botão.
            imagem (objeto, opcional): Imagem exibida no botão.
            comando (função, opcional): Função a ser executada quando o botão for clicado.
        """
        self.__posx = posx
        self.__posy = posy
        self.__janela = janela
        self.__imagem = imagem
        self.__texto = texto
        self.__comando = comando
    
    def botao_padrao(self) -> None:
        """
        Cria um botão personalizado padrão na janela.

        O botão padrão tem um tamanho padrão e pode conter texto e/ou imagem.
        """
        self.__botao = ctk.CTkButton(master=self.__janela, 
                                   width= 187, 
                                   height=82, 
                                   text=self.__texto, 
                                   font=('League Spartan bold',15),
                                   image= self.__imagem, 
                                   compound='left', 
                                   fg_color='#d7ebf8', 
                                   text_color='black', 
                                   corner_radius=0,
                                   command=self.__comando)
        self.__botao.place(x = self.__posx,
                          y = self.__posy)
    
    def botao_menor(self, cor:str) -> None:
        """
        Cria um botão personalizado menor na janela.

        O botão menor tem um tamanho reduzido e pode conter texto e/ou imagem.

        Args:
            cor (str): Cor(em hexadecimal) de fundo do botão.
        """
        self.__botaomenor = ctk.CTkButton(master=self.__janela, 
                                             width=170, 
                                             height=50,
                                             font=('League Spartan bold',17),
                                             fg_color=cor,
                                             corner_radius=0, 
                                             text=self.__texto, 
                                             text_color='black',
                                             command = self.__comando,
                                             image=self.__imagem)
        self.__botaomenor.place(x = self.__posx, y = self.__posy)