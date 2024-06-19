from interface_grafica.menuautomacao.interfaces_auto.IMenuNameAuto import IMenuNameAuto
from tkinter import *
import customtkinter as ctk
from interface_grafica.src.frame import Frame
from interface_grafica.src.automacao import Automacao
from PIL import Image
from time import sleep
from interface_grafica.src.botao import Botao

class MenuNameAuto(IMenuNameAuto):
    """
    Classe que representa o menu para adicionar nome à automação.
    """
    def __init__(self, janela:ctk, auto:Automacao) -> None:
        """
        Inicializa o menu para a definição do nome da automação.

        Argumentos:
            janela(ctk): Janela onde o frame da interface será fixado.
            auto(Automacao): Automação a ser adicionada.
        """
        self.janela = janela
        self.auto = auto

    def criaframe(self) -> None:
        """
        Cria o frame da interface para adicionar um nova automação.
        """
        self.__frame = Frame(self.janela, 'Qual será o nome', 'da automação?')
        self.__frame_name_auto = self.__frame.retorna_frame()
    
    def criar_entry(self) -> None:
        """
        Cria a entry para coletar o nome da automação.
        """
        self.txtbox_name_auto = ctk.CTkEntry(self.__frame_name_auto, 
                                             width=180, height= 40,
                                             font=('League Spartan', 17),
                                             placeholder_text="Nome da automação",
                                             placeholder_text_color="gray", fg_color='#dfedf6', bg_color='white',
                                             corner_radius=15, border_color='white')
        self.txtbox_name_auto.configure(justify = 'center')
        self.txtbox_name_auto.place(x=135,   
                                    y=200)
        
    def botao_confirmar (self) -> None:
        """
        Cria o botão de confirmação para adicionar a automação.
        """
        image = ctk.CTkImage(light_image= Image.open('imagens/check.png'),size=(25,25))
        self.botaoConfirmar = Botao(janela=self.__frame_name_auto,posx=140, posy = 320, texto='Concluir',
                                     imagem=image, comando=self.__adicionar)
        self.botaoConfirmar.botao_menor('#d7ebf8')
    
    def __adicionar(self) -> None:
        """
        Adiciona uma nova automação a planilha principal de automações.
        """
        self.__nome_auto = self.txtbox_name_auto.get().strip()
        self.auto.nome_auto = self.__nome_auto
        if self.auto.adicionar_auto():
            self.__mensagem_confirmacao('      Automação adicionada com sucesso!!')
        else:
            self.__mensagem_confirmacao('Já existe uma automação com esse apelido!')

        from interface_grafica.menuautomacao.MenuAutomações import MenuAutomacoes
        IA = MenuAutomacoes(self.janela)
        IA.executar()
    
    def __mensagem_confirmacao(self, mensagem:str) -> None:
        """
        Exibe uma mensagem de confirmação na interface.

        Args:
            mensagem(str): Texto a ser exibido na mensagem.
        """
        self.texto = ctk.CTkLabel(master=self.__frame_name_auto, 
                                  text=mensagem,
                                  font=('League Spartan', 20), 
                                  fg_color='#ECF4F9', anchor='center')
        self.texto.place(x = 50, y = 400)
        self.__frame_name_auto.update()
        sleep(1)
        
    def executar(self) -> None:
        """
        Coloca o frame na tela.
        """
        self.criaframe()
        self.criar_entry()
        self.botao_confirmar()
        
        