from interface_grafica.src.interfaces_src.IBotaoDinamico import IBotaoDinamico
import customtkinter as ctk
import openpyxl
from interface_grafica.menudispositivos.MenuNewDisp import MenuNewDisp
from abc import ABC, abstractmethod
from interface_grafica.src.botao import Botao
from PIL import Image

class BotaoDinamico(IBotaoDinamico):
    """
    Classe abstrata que representa um botão dinâmico em uma interface gráfica.
    """

    def __init__(self, janela:ctk) -> None:
        """
        Inicializa a classe BotaoDinamico.

        Args:
            janela (ctk): A janela onde o botão será exibido.
        """
        self.janela = janela
        self.nome = []
        self.posicoesx = []
        self.posicoesy = []
        pass
    
    def configura_botao(self, posx: int, posy: int, texto: str, imagem: Image.Image, comando) -> None:
        """
        Configura as propriedades de um botão.

        Args:
            posx (int): A posição x do botão na janela.
            posy (int): A posição y do botão na janela.
            texto (str): O texto exibido no botão.
            imagem (PIL.Image): A imagem exibida no botão.
            comando (function): A função a ser executada quando o botão for clicado.
        """
        self.botao = Botao(janela=self.janela, posx=posx, posy=posy, texto=texto,
                           imagem=imagem, comando=comando)
        self.botao.botao_padrao()
        
    def importar_posicoes(self) -> None:
        """
        Importa as posições dos botões a partir de um arquivo Excel.
        """
        self.workbook = openpyxl.load_workbook('planilhas/posicoes.xlsx')
        self.planilha_1 = self.workbook['Sheet1']
        
        for linha in self.planilha_1.iter_rows(min_row=1, values_only=True):
            self.posicoesx.append(linha[0])
            self.posicoesy.append(linha[1])

    def importa_nomes(self) -> None:
        """
        Importa os nomes dos botões a partir de uma planilha.
        """
        self.nome = self.planilha.retorna_coluna("A")

    @abstractmethod
    def abre_imagens(self) -> None:
        """
        Abre as imagens dos botões.
        """
        pass
    
    @abstractmethod
    def insere_botoes(self) -> None:
        """
        Insere os botões na interface gráfica.
        """
        pass
    
    