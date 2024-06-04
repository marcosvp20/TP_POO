import time
import customtkinter as ctk
from PIL import Image

class TelaInicial:
    def __init__(self, janela:ctk) -> None:
        """
        Classe responsável por criar a tela inicial da aplicação.
        """
        self.janela = janela
        
    def cria_frame(self) -> None:
        """
        Cria o frame da tela inicial.
        """
        self.frame = ctk.CTkFrame(master=self.janela,
                                  width=450,
                                  height=660,
                                  fg_color='transparent')
        bg = ctk.CTkImage(light_image=Image.open('imagens/inicializacao.png'), 
                          size=(450,750))
        
        label = ctk.CTkLabel(self.frame, 
                             width=450, 
                             height= 660, 
                             image=bg, 
                             text='')
        label.place(x = 0, y = 0)
    
    def cria_texto(self, texto:str) -> None:
        """
        Cria o texto de saudação na tela inicial.
        """
        self.texto_ola = ctk.CTkLabel(master=self.frame,
                                            text=f'Olá,',
                                             font=('League Spartan bold', 35),
                                             fg_color='white',
                                             text_color='black')
        self.texto_bomdia = ctk.CTkLabel(master=self.frame,
                                            text=f'{texto}',
                                             font=('League Spartan bold', 35),
                                             fg_color='white',
                                             text_color='black')
        
        self.texto_ola.place(x = 30, y = 50)
        self.texto_bomdia.place(x = 30, y = 100)
    
    def importar_hora(self) -> None:
        """
        Importa a hora atual do sistema.
        """
        self.hora_atual = time.localtime().tm_hour
        
    def executar(self) -> None:
        """
        Executa a criação da tela inicial.
        """
        self.cria_frame()
        self.importar_hora()
        if self.hora_atual < 12 and self.hora_atual > 0:
            self.cria_texto('Bom dia!')
            
        elif self.hora_atual > 11 and self.hora_atual < 18:
            self.cria_texto('Boa tarde!')
        
        elif self.hora_atual > 17 and self.hora_atual <= 23:
            self.cria_texto('Boa noite!')
        
        self.frame.place(x = 0, y = 0)