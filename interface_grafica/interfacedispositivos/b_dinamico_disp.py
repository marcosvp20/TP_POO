import customtkinter as ctk
from src.planilha import Planilha
from interfacedispositivos.InterfaceDispositivos import InterfaceNewDisp
from PIL import Image
from src.botao_dinamico import BotaoDinamico
from src.botao import Botao

class BotaoDinamicoDisp(BotaoDinamico):
    
    """Classe que representa um botão dinâmico para dispositivos."""

    def __init__(self, janela:ctk, planilha:str) -> None:
        """
        Inicializa a classe BotaoDinamicoDisp.
        """
        super().__init__(janela)
        self.planilha = Planilha(planilha)
        self.quantidade = self.planilha.retorna_quantidade_dispositivos()
        self.tipos = self.planilha.retorna_tipos()
        self.insere_botoes(planilha)

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

    def insere_botoes(self, planilha) -> None:
        """
        Insere os botões na interface.
        """
        from interfacedispositivos.InterfaceAC import InterfaceAC
        from interfacedispositivos.InterfaceLamp import InterfaceLamp
        from interfacedispositivos.InterfaceTV import InterfaceTV
        
        self.importar_posicoes()
        self.importa_nomes()
        self.abre_imagens()
        if self.quantidade > 0:
            for i in range(0, self.quantidade):
                
                match(self.tipos[i]):
                    case 'A/C':
                        interfaceAC = InterfaceAC(self.janela, self.nome[i], self.planilha)
                        self.configura_botao(posx=int(self.posicoesx[i]), posy=int(self.posicoesy[i]),
                        texto=self.nome[i], imagem=self.imagem_ac, comando= interfaceAC.executar)
                    case 'Lâmpada':
                        interfaceLamp = InterfaceLamp(self.janela, self.nome[i], self.planilha)
                        self.configura_botao(posx=int(self.posicoesx[i]), posy=int(self.posicoesy[i]),
                        texto=self.nome[i], imagem=self.imagem_lamp, comando= interfaceLamp.executar)
                    case 'Televisor':
                        interfaceTV = InterfaceTV(self.janela, self.nome[i], self.planilha)
                        self.configura_botao(posx=int(self.posicoesx[i]), posy=int(self.posicoesy[i]),
                        texto=self.nome[i], imagem=self.imagem_tv, comando= interfaceTV.executar)

    def botao_add (self, posx, posy ) -> None:
        """
        Adiciona um botão para adicionar um novo dispositivo.
        """
        new_disp = InterfaceNewDisp(self.janela)
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