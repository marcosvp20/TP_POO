import customtkinter as ctk
from planilha import Planilha

class BotaoDinamico:

    def __init__(self, janela:ctk, comando = None) -> None:
        self.janela = janela
        self.comando = comando
        self.nome = []
        self.planilha = Planilha('objetos.xlsx')
    
    def configura_botao(self):
        self.botao = ctk.CTkButton(master=self.janela, 
                                   width= 187, 
                                   height=82, 
                                   text=None, 
                                   font=('League Spartan bold',15),
                                   image= None, 
                                   compound='left', 
                                   fg_color='#d7ebf8', 
                                   text_color='black', 
                                   corner_radius=0,
                                   command= self.comando)
        
    def importar_posicoes(self) -> None:
            with open('posicoes.txt','r') as arquivo:
                for linha in arquivo:
                    self.posicoes = linha.strip().split(',')

    def importa_nomes(self) -> None:
        self.nome = self.planilha.retorna_nome()
        