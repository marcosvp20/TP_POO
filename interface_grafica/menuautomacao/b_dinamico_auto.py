import customtkinter as ctk
from interface_grafica.src.planilha import Planilha
from interface_grafica.menuautomacao.MenuNewAuto import MenuNewAuto
from PIL import Image
from interface_grafica.src.botao_dinamico import BotaoDinamico
from interface_grafica.src.automacao import Automacao
from interface_grafica.src.botao import Botao

class BotaoDinamicoAuto(BotaoDinamico):
    """
    Classe que representa um botão dinâmico para as automações.
    """
    def __init__(self, janela:ctk) -> None:
        """
        Inicializa a classe BotaoDinamicoAuto.

        Argumentos:
            janela(ctk): Janela referência na adição dos botões.
        """
        super().__init__(janela)
        self.planilha = Planilha('planilhas/automacoes.xlsx')
        self.importa_nomes()
        self.quantidade = len(self.nome)
        self.insere_botoes()
    
    def configura_botao(self, posx:int, posy:int, texto:str, imagem:Image.Image, comando:callable) -> None:
        """
        Configura um botão dinâmico.
        
        Args:
        posx (int): Posição horizontal do botão na janela.
        posy (int): Posição vertical do botão na janela.
        texto (str): Texto exibido no botão.
        imagem (image.image): Imagem exibida no botão.
        comando (callable): Função a ser executada quando o botão for clicado.
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
    
    def abre_imagens(self) -> None:
        """
        Abre as imagens dos botões.
        """
        self.imagem_automacao = ctk.CTkImage(Image.open('imagens/acao.png'),size=(30,30))
    
    def insere_botoes(self) -> None:
        """
        Insere os botões no frame.
        """
        from interface_grafica.menuautomacao.MenuExecutarAuto import MenuAutomacao

        self.importar_posicoes()
        self.abre_imagens()
        if not self.planilha.verifica_se_esta_vazio():
            if self.quantidade > 0:
                for i in range(0, self.quantidade):
                    self.configura_botao(posx=int(self.posicoesx[i]), posy=int(self.posicoesy[i]),
                                        texto='"'+self.nome[i]+'"', imagem=self.imagem_automacao, comando= MenuAutomacao(self.janela, self.nome[i]).executar)
            
                
    def botao_add (self, posx:int, posy:int) -> None:
        """
        Adiciona um novo botão de adicionar dispositivo.
        """
        new_auto = MenuNewAuto(self.janela)
        imagem = ctk.CTkImage(light_image= Image.open('imagens/plus.png'),size=(25,25))
        self.botaoAdd = Botao(janela=self.janela, posx=posx, posy=posy, texto='Adicionar\nAutomação',
                              imagem=imagem, comando=new_auto.executar)
        self.botaoAdd.botao_padrao()

    def insere_botao_add(self) -> None:
        """
        Insere o botão de adicionar dispositivo no frame.
        """
        if self.quantidade < 6:
            if self.planilha.verifica_se_esta_vazio():
                self.botao_add(self.posicoesx[0], self.posicoesy[0])
            else:
                self.botao_add(self.posicoesx[self.quantidade], self.posicoesy[self.quantidade])
    
