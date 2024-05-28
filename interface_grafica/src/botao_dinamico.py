import customtkinter as ctk
from src.planilha import Planilha
import openpyxl
from interfacedispositivos.InterfaceNewDisp import InterfaceNewDisp
from PIL import Image

class BotaoDinamico:

    def __init__(self, janela:ctk, comando = None) -> None:
        self.janela = janela
        self.comando = comando
        self.nome = []
        self.posicoesx = []
        self.posicoesy = []
        self.planilha = Planilha('objetos.xlsx')
        self.quantidade = self.planilha.retorna_quantidade_dispositivos()
        self.tipos = self.planilha.retorna_tipos()
        self.insere_botao()
    
    def configura_botao(self, posx, posy, texto, imagem):
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
                                   command= self.comando)
        self.botao.place(x = posx, y = posy)
        
    def botao_add (self, posx, posy ) -> None:
        new_disp = InterfaceNewDisp(self.janela)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/plus.png'),size=(25,25))
        self.botao_adicionar = self.botao = ctk.CTkButton(master=self.janela, 
                                   width= 187, 
                                   height=82, 
                                   text='Adicionar\nDispositivo', 
                                   font=('League Spartan bold',15),
                                   image= imagem, 
                                   compound='left', 
                                   fg_color='#d7ebf8', 
                                   text_color='black', 
                                   corner_radius=0,
                                   command=new_disp.executar)
        self.botao_adicionar.place(x = posx, 
                                y = posy) 
            
    def importar_posicoes(self) -> None:
        self.workbook = openpyxl.load_workbook('posicoes.xlsx')
        self.planilha_1 = self.workbook['Sheet1']
        
        for linha in self.planilha_1.iter_rows(min_row=1, values_only=True):
            self.posicoesx.append(linha[0])
            self.posicoesy.append(linha[1])
        

    def importa_nomes(self) -> None:
        self.nome = self.planilha.retorna_nome()
    
    def insere_botao(self) -> None:
        self.importar_posicoes()
        self.importa_nomes()
        self.abre_imagens()
        if self.quantidade > 0:
            for i in range(0, self.quantidade):
                
                match(self.tipos[i]):
                    case 'A/C':
                        self.configura_botao(posx=int(self.posicoesx[i]), posy=int(self.posicoesy[i]),
                                        texto=self.nome[i], imagem=self.imagem_ac)
                    case 'Lâmpada':
                        self.configura_botao(posx=int(self.posicoesx[i]), posy=int(self.posicoesy[i]),
                        texto=self.nome[i], imagem=self.imagem_lamp)
                    case 'Televisor':
                        self.configura_botao(posx=int(self.posicoesx[i]), posy=int(self.posicoesy[i]),
                        texto=self.nome[i], imagem=self.imagem_tv)
                    
        if self.quantidade < 6:
            self.botao_add(self.posicoesx[self.quantidade], self.posicoesy[self.quantidade])
    
    def abre_imagens(self) -> None:
        self.imagem_ac = ctk.CTkImage(Image.open('imagens/arcondicionado.png'),size=(40,40))
        self.imagem_lamp = ctk.CTkImage(Image.open('imagens/lampada.png'),size=(40,40))
        self.imagem_tv = ctk.CTkImage(Image.open('imagens/tv.png'),size=(40,40))

# jan = ctk.CTk()
# jan.geometry('800x800')
# bot = BotaoDinamico(jan)
# bot.insere_botao()
# jan.mainloop()