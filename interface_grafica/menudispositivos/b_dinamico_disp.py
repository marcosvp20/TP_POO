import customtkinter as ctk
from src.planilha import Planilha
from menudispositivos.MenuNewDisp import MenuNewDisp
from PIL import Image
from src.botao_dinamico import BotaoDinamico
from src.botao import Botao

class BotaoDinamicoDisp(BotaoDinamico):
    """
    Classe que representa um botão dinâmico para dispositivos.
    """

    def __init__(self, janela:ctk, planilha:Planilha) -> None:
        """
        Inicializa a classe BotaoDinamicoDisp.

        Argumentos:
            janela(ctk): Janela referência para posicionamento dos botões.
            planilha(Planilha): Planilha com os dados a serem utilizados.
        """
        super().__init__(janela)
        self.planilha = planilha  
        self.quantidade = self.planilha.retorna_quantidade_linhas()
        self.tipos = self.planilha.retorna_tipos()
        self.insere_botoes()

    def configura_botao(self, posx, posy, texto, imagem, comando):
        """
        Configura um botão dinâmico.
        """
        super().configura_botao(posx, posy, texto, imagem, comando)

    def importar_posicoes(self) -> None:
        """
        Importa as posições dos botões.
        """
        super().importar_posicoes()

    def importa_nomes(self) -> None:
        """
        Importa os nomes dos dispositivos.
        """
        super().importa_nomes()
    
    def abre_imagens(self) -> None:
        """
        Abre as imagens dos dispositivos.
        """
        self.imagem_ac = ctk.CTkImage(Image.open('imagens/arcondicionado.png'),size=(40,40))
        self.imagem_lamp = ctk.CTkImage(Image.open('imagens/lampada.png'),size=(40,40))
        self.imagem_tv = ctk.CTkImage(Image.open('imagens/tv.png'),size=(40,40))

    def insere_botoes(self) -> None:
        """
        Insere os botões referentes aos dispositivos disponíveis na interface.
        """
        from menudispositivos.MenuAC import MenuAC
        from menudispositivos.MenuLamp import MenuLamp
        from menudispositivos.MenuTV import MenuTV
        
        self.importar_posicoes()
        self.importa_nomes()
        self.abre_imagens()
        if self.quantidade > 0:
            for i in range(0, self.quantidade):
                match(self.tipos[i]):
                    case 'A/C':
                        interfaceAC = MenuAC(self.janela, self.nome[i], self.planilha)
                        self.configura_botao(posx=int(self.posicoesx[i]), posy=int(self.posicoesy[i]),
                        texto=self.nome[i], imagem=self.imagem_ac, comando= interfaceAC.executar)
                    case 'Lâmpada':
                        interfaceLamp = MenuLamp(self.janela, self.nome[i], self.planilha)
                        self.configura_botao(posx=int(self.posicoesx[i]), posy=int(self.posicoesy[i]),
                        texto=self.nome[i], imagem=self.imagem_lamp, comando= interfaceLamp.executar)
                    case 'Televisor':
                        menuTV = MenuTV(self.janela, self.nome[i], self.planilha)
                        self.configura_botao(posx=int(self.posicoesx[i]), posy=int(self.posicoesy[i]),
                        texto=self.nome[i], imagem=self.imagem_tv, comando= menuTV.executar)

    def botao_add (self, posx, posy) -> None:
        """
        Adiciona um botão para adicionar um novo dispositivo.
        """
        new_disp = MenuNewDisp(self.janela, self.planilha)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/plus.png'),size=(25,25))
        self.botaoAdd = Botao(janela=self.janela,  posx=posx, posy=posy, texto='Adicionar\nDispositivo',
                              imagem=imagem, comando=new_disp.executar)
        self.botaoAdd.botao_padrao()
        

    def insere_botao_add(self) -> None:
        """
        Insere o botão para adicionar um novo dispositivo.
        """
        if self.quantidade < 6:
            self.botao_add(self.posicoesx[self.quantidade], self.posicoesy[self.quantidade])