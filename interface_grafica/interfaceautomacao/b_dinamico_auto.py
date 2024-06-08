import customtkinter as ctk
from src.planilha import Planilha
from interfaceautomacao.InterfaceNewAuto import interfaceNewAuto
from PIL import Image
from src.botao_dinamico import BotaoDinamico

class BotaoDinamicoAuto(BotaoDinamico):
    def __init__(self, janela:ctk) -> None:
        super().__init__(janela)
        self.planilha = Planilha('automacoes.xlsx')
        self.quantidade = self.planilha.retorna_quantidade_dispositivos()
        self.insere_botoes()
    
    def configura_botao(self, posx, posy, texto, imagem, comando):
        super().configura_botao(posx, posy, texto, imagem, comando)
            
    def importar_posicoes(self) -> None:
        super().importar_posicoes()
   
    def importa_nomes(self) -> None:
        super().importa_nomes()
    
    def abre_imagens(self) -> None:
        self.imagem_automacao = ctk.CTkImage(Image.open('imagens/acao.png'),size=(30,30))
    
    def insere_botoes(self) -> None:
        self.importar_posicoes()
        self.importa_nomes()
        self.abre_imagens()
        if self.quantidade > 0:
            for i in range(0, self.quantidade):
                self.configura_botao(posx=int(self.posicoesx[i]), posy=int(self.posicoesy[i]),
                                     texto='"'+self.nome[i]+'"', imagem=self.imagem_automacao, comando= None)
                
    def botao_add (self, posx, posy ) -> None:
        new_auto = interfaceNewAuto(self.janela)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/plus.png'),size=(25,25))
        self.botao_add = self.botao = ctk.CTkButton(master=self.janela, 
                                   width= 187, 
                                   height=82, 
                                   text='Adicionar\nDispositivo', 
                                   font=('League Spartan bold',15),
                                   image= imagem, 
                                   compound='left', 
                                   fg_color='#d7ebf8', 
                                   text_color='black', 
                                   corner_radius=0,
                                   command=new_auto.executar)
        self.botao_add.place(x = posx, 
                             y = posy) 

    def insere_botao_add(self) -> None:
        if self.quantidade < 6:
            self.botao_add(self.posicoesx[self.quantidade], self.posicoesy[self.quantidade])
    
