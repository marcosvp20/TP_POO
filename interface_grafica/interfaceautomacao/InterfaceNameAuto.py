from tkinter import *
import customtkinter as ctk
from src.frame import Frame
from src.automacao import Automacao
from PIL import Image
from time import sleep

class InterfaceNameAuto:
    def __init__(self, janela:ctk) -> None:
        """
        Classe responsável por criar a interface para adicionar uma nova automação

        Args:
            janela(ctk): Janela onde o frame da interface será fixado
        """
        self.janela = janela

    def criaframe(self) -> None:
        """
        Cria o frame da interface para adicionar um nova automação.
        """

        self.frame_name_auto = Frame(self.janela, 'Qual será o nome', 'da automação?').frame
        
        self.txtbox_name_auto = ctk.CTkEntry(self.frame_name_auto, 
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
        self.botao_adicionar = ctk.CTkButton(master=self.frame_name_auto, 
                                             width=170, 
                                             height=50,
                                             font=('League Spartan bold',17),
                                             fg_color='#d7ebf8',
                                             corner_radius=0, 
                                             text='Concluir', 
                                             text_color='black',
                                             command = self.__adicionar,
                                             image=image)
        self.botao_adicionar.place(x = 140, y = 320)
    
    def __adicionar(self) -> None:
        """
        Adiciona uma nova automação a planilha principal de automações.
        """
        self.__nome_auto = self.txtbox_name_auto.get().strip()
        auto = Automacao(self.__nome_auto)
        if auto.adicionar_auto():
            self.__mensagem_confirmacao('Automação adicionada com sucesso!!')
        else:
            self.__mensagem_confirmacao('Já existe uma automação com esse apelido!')

        from interfaceautomacao.interfaceAutomações import interfaceAutomacoes
        IA = interfaceAutomacoes(self.janela)
        IA.executar()
    
    def __mensagem_confirmacao(self,mensagem:str) -> None:
        """
        Exibe uma mensagem de confirmação na interface.
        """
        self.texto = ctk.CTkLabel(master=self.frame_name_auto, 
                                  text=mensagem,
                                    font=('League Spartan', 20), 
                                    fg_color='#ECF4F9', anchor='center')
        self.texto.place(x = 50, y = 400)
        self.frame_name_auto.update()
        sleep(1)
        
    def executar(self) -> None:
        """
        Coloca o frame na tela.
        """
        self.criaframe()
        self.botao_confirmar()
        
        