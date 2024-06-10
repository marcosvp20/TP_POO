import customtkinter as ctk
from src.planilha import Planilha
from interfaceautomacao.InterfaceNewAuto import interfaceNewAuto
from PIL import Image
from src.botao_dinamico import BotaoDinamico
from src.automacao import Automacao

class BotaoDinamicoAuto(BotaoDinamico):

    """Classe que representa um botão dinâmico para as automações."""

    def __init__(self, janela:ctk) -> None:
        """
        Inicializa a classe BotaoDinamicoAuto.
        """
        super().__init__(janela)
        self.planilha = Planilha('planilhas/automacoes.xlsx')
        self.importa_nomes()
        self.quantidade = len(self.nome)
        print(self.quantidade)
        self.insere_botoes()
    
    def configura_botao(self, posx, posy, texto, imagem, comando):
        """
        Configura um botão dinâmico.
        """
        super().configura_botao(posx, posy, texto, imagem, comando)
            
    def importar_posicoes(self) -> None:
        """
        Importa as posições dos botões a partir de um arquivo.
        """
        super().importar_posicoes()
   
    def importa_nomes(self) -> None:
        """
        Importa os nomes dos botões a partir de um arquivo.
        """
        auto = Automacao(None)
        self.nome = auto.retorna_nomes_auto()
        
        #super().importa_nomes()
    
    def abre_imagens(self) -> None:
        """
        Abre as imagens dos botões.
        """
        self.imagem_automacao = ctk.CTkImage(Image.open('imagens/acao.png'),size=(30,30))
    
    def insere_botoes(self) -> None:
        """
        Insere os botões no frame.
        """
        self.importar_posicoes()
        self.abre_imagens()
        if not self.planilha.verifica_se_esta_vazio():

            if self.quantidade > 0:
                for i in range(0, self.quantidade):
                    self.configura_botao(posx=int(self.posicoesx[i]), posy=int(self.posicoesy[i]),
                                        texto='"'+self.nome[i]+'"', imagem=self.imagem_automacao, comando= None)
            
                
    def botao_add (self, posx, posy ) -> None:
        """
        Adiciona um novo botão de adicionar dispositivo.
        """
        new_auto = interfaceNewAuto(self.janela)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/plus.png'),size=(25,25))
        self.botao_add = self.botao = ctk.CTkButton(master=self.janela, 
                                   width= 187, 
                                   height=82, 
                                   text='Adicionar\nAutomação', 
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
        """
        Insere o botão de adicionar dispositivo no frame.
        """
        if self.quantidade < 6:
            if self.planilha.verifica_se_esta_vazio():
                self.botao_add(self.posicoesx[0], self.posicoesy[0])
            else:
                self.botao_add(self.posicoesx[self.quantidade], self.posicoesy[self.quantidade])
    
