import customtkinter as ctk
from src.planilha import Planilha
import openpyxl
from interfacedispositivos.InterfaceNewDisp import InterfaceNewDisp
from PIL import Image
from abc import ABC, abstractmethod

class BotaoDinamico(ABC):

    def __init__(self, janela:ctk) -> None:
        self.janela = janela
        self.nome = []
        self.posicoesx = []
        self.posicoesy = []
        pass
    
    def configura_botao(self, posx, posy, texto, imagem, comando):
        self.botao = ctk.CTkButton(master=self.janela,
                                   width= 187, 
                                   height=82, 
                                   text=texto, 
                                   font=('League Spartan bold',15),
                                   image= imagem, 
                                   compound='left', 
                                   fg_color='#d7ebf8', 
                                   text_color='black', 
                                   corner_radius=0,
                                   command= comando)
        self.botao.place(x = posx, y = posy)
        
    def importar_posicoes(self) -> None:
        self.workbook = openpyxl.load_workbook('posicoes.xlsx')
        self.planilha_1 = self.workbook['Sheet1']
        
        for linha in self.planilha_1.iter_rows(min_row=1, values_only=True):
            self.posicoesx.append(linha[0])
            self.posicoesy.append(linha[1])

    def importa_nomes(self) -> None:
        self.nome = self.planilha.retorna_nome()

    @abstractmethod
    def abre_imagens(self) -> None:
        pass
    
    @abstractmethod
    def insere_botoes(self) -> None:
        pass
    
    