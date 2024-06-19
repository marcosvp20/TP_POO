from tkinter import *
from PIL import Image
import customtkinter as ctk
import time
from interface_grafica.src.planilha import Planilha
from interface_grafica.src.arcondicionado import ArCondicionado
from interface_grafica.src.lampada import Lampada
from interface_grafica.src.televisao import Televisao
from interface_grafica.src.frame import Frame
from interface_grafica.src.botao import Botao


class MenuNameDisp:
    """
    Classe responsável por criar a interface para adicionar um nome ao novo dispositivo.
    """
    def __init__(self, janela:ctk, tipo:str, planilha:Planilha) -> None:
        """
        Inicializa o menu de definição de nome do dispositivo.

        Argumentos:
            janela(ctk): Janela referência à inicialização do menu.
            tipo(str): Tipo do objeto em questão.
            planilha(Planilha): Planilha que contém os dados a serem utilizados.
        """
        self.janela = janela
        self.tipo = tipo
        self.planilha = planilha

    def criaframe(self) -> None:
        """
        Cria o frame da interface para adicionar um novo dispositivo.
        """
        self.__frame = Frame(self.janela, 'Qual será o nome', 'do dispositivo?')
        self.__frame_name_disp = self.__frame.retorna_frame()
        
        self.txtbox_name_disp = ctk.CTkEntry(self.__frame_name_disp, 
                                             width=180, height= 40,
                                             font=('League Spartan', 17),
                                             placeholder_text="Nome do dispositivo",
                                             placeholder_text_color="gray", fg_color='#dfedf6', bg_color='white',
                                             corner_radius=15, border_color='white')
        self.txtbox_name_disp.configure(justify = 'center')
        self.txtbox_name_disp.place(x=135,   
                                    y=200)
        
    def botao_confirmar (self) -> None:
        """
        Cria o botão de confirmação para adicionar o dispositivo.
        """
        image = ctk.CTkImage(light_image= Image.open('imagens/check.png'),size=(25,25))
        self.botao_adicionar = Botao(self.__frame_name_disp, posx=140, posy=320, texto='Concluir',
                                     imagem=image, comando=self.adicionar)
        self.botao_adicionar.botao_menor('#d7ebf8')
        
    def adicionar(self) -> None:
        """
        Adiciona o dispositivo à planilha de objetos.
        """
        self.__frame_name_disp.update()
        if self.tipo:
            self.new_name = self.txtbox_name_disp.get().strip()
            if self.new_name:
                match(self.tipo):
                    case "A/C":
                        if ArCondicionado(self.new_name, self.planilha).salvar():
                            self.mensagem_confirmacao('O dispositivo foi adicionado com sucesso!!')
                            self.parar_execucao()
                            self.__frame_name_disp.update()
                        elif self.planilha.verifica_se_objeto_existe(self.new_name):
                            self.mensagem_confirmacao('Um dispositivo com esse apelido já existe!')
                            self.apagar_mensagem_confirmacao()
                            self.__frame_name_disp.update()
                    case "Lâmpada":
                        if Lampada(self.new_name, self.planilha).salvar():
                            self.mensagem_confirmacao('O dispositivo foi adicionado com sucesso!!')
                            self.parar_execucao()
                            self.__frame_name_disp.update()
                        elif self.planilha.verifica_se_objeto_existe(self.new_name):
                            self.mensagem_confirmacao('Um dispositivo com esse apelido já existe!')
                            self.apagar_mensagem_confirmacao()
                            self.__frame_name_disp.update()
                    case "Televisor":
                        if Televisao(self.new_name, self.planilha).salvar():
                            self.mensagem_confirmacao('O dispositivo foi adicionado com sucesso!!')
                            self.parar_execucao()
                            self.__frame_name_disp.update()
                        elif self.planilha.verifica_se_objeto_existe(self.new_name):
                            self.mensagem_confirmacao('Um dispositivo com esse apelido já existe!')
                            self.apagar_mensagem_confirmacao()
                            self.__frame_name_disp.update()
                            
    def mensagem_confirmacao(self, mensagem:str) -> None:
        """
        Exibe uma mensagem de confirmação na interface.

        Argumentos:
            mensagem(str): Mensagem de confirmação a ser exibida.
        """
        self.texto = ctk.CTkLabel(master=self.__frame_name_disp, 
                                  text=mensagem,
                                    font=('League Spartan', 20), 
                                    fg_color='#ECF4F9')
        self.texto.place(x = 50, y = 400)
        self.__frame_name_disp.update()
        time.sleep(1)
        
    def apagar_mensagem_confirmacao(self) -> None:
        """
        Apaga a mensagem de confirmação da interface.
        """
        self.texto.destroy()
        
    def parar_execucao(self) -> None:
        """
        Para a execução da interface e retorna para o menu de dispositivos.
        """
        from interface_grafica.menudispositivos.MenuDispositivos import MenuDispositivos

        self.__frame.destroy()
        MenuDispositivos(self.janela).executar()
        
    def executar(self) -> None:
        """
        Executa a interface para adicionar um novo dispositivo.
        """
        self.criaframe()
        self.botao_confirmar()
        