import customtkinter as ctk
from PIL import Image
from time import sleep

class Frame:
    """
    Classe que representa um frame na interface gráfica.
    """
    def __init__(self, janela: ctk, texto1: str, texto2:str = '') -> None:
        """
        Inicializa o frame.
 Args:
            janela (ctk): Objeto da janela onde o frame será exibido.
            texto1 (str): Texto a ser exibido na primeira caixa de texto.
            texto2 (str, opcional): Texto a ser exibido na segunda caixa de texto (se houver).

        Attributes:
            __janela (ctk): Objeto da janela onde o frame será exibido.
            __texto1 (str): Texto a ser exibido na primeira caixa de texto.
            __texto2 (str): Texto a ser exibido na segunda caixa de texto (se houver).
            __frame (ctk): Objeto do frame.
            caixa_de_texto1 (ctk): Objeto da primeira caixa de texto.
            caixa_de_texto2 (ctk): Objeto da segunda caixa de texto (opcional).
        """
        self.__janela = janela
        self.__texto1 = texto1
        self.__texto2 = texto2

    def retorna_frame(self) -> ctk:
        """
        Retorna o frame.

        Returns:
            ctk: Objeto do frame criado na interface gráfica.
        """
        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), 
                          size=(450,750))
        self.__frame = ctk.CTkFrame(self.__janela, 
                                  width=450, 
                                  height=660,
                                  fg_color= "transparent")
        self.__frame.place(x=0, 
                         y=0)
        
        label = ctk.CTkLabel(self.__frame, 
                             width=450, 
                             height= 660, 
                             image=bg, 
                             text='')
        
        self.caixa_de_texto1 = ctk.CTkLabel(self.__frame,
                                           text=self.__texto1,
                                           font=('League Spartan', 30),
                                           fg_color='white')
        
        self.caixa_de_texto1.place(x = 10,
                                  y = 60)
        
        label.place(x = 0, 
                    y = 0)
        
        if self.__texto2 != '':
            self.caixa_de_texto2 = ctk.CTkLabel(self.__frame,
                                             text=self.__texto2,
                                             font=('League Spartan', 30),
                                             fg_color='white')
            self.caixa_de_texto2.place(x = 10,
                                       y = 100)
    
        return self.__frame

    def mensagem(self, mensagem:str) -> None:
        """
        Exibe uma mensagem na interface do ar condicionado.

        Args:
            mensagem (str): Mensagem a ser exibida.
        """
        self.texto = ctk.CTkLabel(master=self.__frame, 
                                  text=mensagem, 
                                  font=('League Spartan', 20), 
                                  fg_color='#CEE2EF')
        self.texto.place(x=85, y=620)
        self.__frame.update()
        sleep(1)
    
    def destroy(self) -> None:
        """
        Destroi o frame
        """
        self.__frame.destroy()
