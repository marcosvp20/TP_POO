from tkinter import *
from PIL import Image
import customtkinter as ctk
from interfacedispositivos.botao_disp import Botao
import time
from src.planilha import Planilha
from src.arcondicionado import ArCondicionado
from src.lampada import Lampada
from src.televisao import Televisao
from src.frame import Frame

class InterfaceNameDisp:
    def __init__(self, janela, tipo) -> None:
        """
        Classe responsável por criar a interface para adicionar um novo dispositivo.
        """
        self.janela = janela
        self.tipo = tipo
        self.planilha = Planilha('planilhas/objetos.xlsx')

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
        self.botao_adicionar = ctk.CTkButton(master=self.__frame_name_disp, 
                                             width=170, 
                                             height=50,
                                             font=('League Spartan bold',17),
                                             fg_color='#d7ebf8',
                                             corner_radius=0, 
                                             text='Concluir', 
                                             text_color='black',
                                             command = self.adicionar,
                                             image=image)
        self.botao_adicionar.place(x = 140, y = 320)
        
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
                        if ArCondicionado(self.new_name, 'planilhas/objetos.xlsx').salvar():
                            self.mensagem_confirmacao('O dispositivo foi adicionado com sucesso!!')
                            self.parar_execucao()
                            self.__frame_name_disp.update()
                        elif self.planilha.verifica_se_objeto_existe(self.new_name):
                            self.mensagem_confirmacao('Um dispositivo com esse apelido já existe!')
                            self.apagar_mensagem_confirmacao()
                            self.__frame_name_disp.update()
                    case "Lâmpada":
                        if Lampada(self.new_name, 'planilhas/objetos.xlsx').salvar():
                            self.mensagem_confirmacao('O dispositivo foi adicionado com sucesso!!')
                            self.parar_execucao()
                            self.__frame_name_disp.update()
                        elif self.planilha.verifica_se_objeto_existe(self.new_name):
                            self.mensagem_confirmacao('Um dispositivo com esse apelido já existe!')
                            self.apagar_mensagem_confirmacao()
                            self.__frame_name_disp.update()
                    case "Televisor":
                        if Televisao(self.new_name, 'planilhas/objetos.xlsx').salvar():
                            self.mensagem_confirmacao('O dispositivo foi adicionado com sucesso!!')
                            self.parar_execucao()
                            self.__frame_name_disp.update()
                        elif self.planilha.verifica_se_objeto_existe(self.new_name):
                            self.mensagem_confirmacao('Um dispositivo com esse apelido já existe!')
                            self.apagar_mensagem_confirmacao()
                            self.__frame_name_disp.update()
                            
    def mensagem_confirmacao(self,mensagem) -> None:
        """
        Exibe uma mensagem de confirmação na interface.
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
        from interfacedispositivos.InterfaceDispositivos import interfaceDispositivos

        self.__frame_name_disp.destroy()
        interfaceDispositivos(self.janela).executar()
        
    def executar(self) -> None:
        """
        Executa a interface para adicionar um novo dispositivo.
        """
        self.criaframe()
        self.botao_confirmar()
        