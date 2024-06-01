from tkinter import *
from PIL import Image
import customtkinter as ctk
from interfacedispositivos.botao_disp import Botao
import time
from src.planilha import Planilha
from src.arcondicionado import ArCondicionado
from src.lampada import Lampada
from src.televisao import Televisao

class InterfaceNameDisp:
    def __init__(self, janela, tipo, frame_anterior:ctk) -> None:
        """
        Classe responsável por criar a interface para adicionar um novo dispositivo.
        """
        self.frame_anterior = frame_anterior
        self.janela = janela
        self.tipo = tipo
        self.planilha = Planilha('objetos.xlsx')

    def criaframe(self) -> None:
        """
        Cria o frame da interface para adicionar um novo dispositivo.
        """
        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), 
                          size=(500,750))
        self.frame_new_disp = ctk.CTkFrame(self.janela, 
                                           width=450, 
                                           height=660,
                                           fg_color= "transparent")
        self.frame_new_disp.place(x=0, 
                                 y=0)
        
        label = ctk.CTkLabel(self.frame_new_disp, 
                             width=450, 
                             height= 660, 
                             image=bg, 
                             text='')
        
        label.place(x = 0, 
                    y = 0)
        
        self.caixa_de_texto1 = ctk.CTkLabel(self.frame_new_disp,
                                             text='Qual será o nome',
                                             font=('League Spartan', 30),
                                             fg_color='white')
        self.caixa_de_texto1.place(x = 10,
                                    y = 60)
        
        self.caixa_de_texto2 = ctk.CTkLabel(self.frame_new_disp,
                                             text='do dispositivo?',
                                             font=('League Spartan', 30),
                                             fg_color='white')
        self.caixa_de_texto2.place(x = 10,
                                    y = 100)
        
        self.txtbox_name_disp = ctk.CTkEntry(self.frame_new_disp, 
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
        self.botao_adicionar = ctk.CTkButton(master=self.frame_new_disp, 
                                             width=170, 
                                             height=50,
                                             font=('League Spartan bold',17),
                                             fg_color='#d7ebf8',
                                             corner_radius=0, 
                                             text='Concluir', 
                                             text_color='black',
                                             command = self.adicionar)
        self.botao_adicionar.place(x = 140, y = 320)
        
    def adicionar(self) -> None:
        """
        Adiciona o dispositivo à planilha de objetos.
        """
        self.frame_new_disp.update()
        if self.tipo:
            self.new_name = self.txtbox_name_disp.get().strip()
            print(self.new_name)
            if self.new_name:
                match(self.tipo):
                    case "A/C":
                        if ArCondicionado(self.new_name).salvar():
                            print("AC adicionado")
                            self.mensagem_confirmacao('Dispositivo adicionado com sucesso!!')
                            self.parar_execucao()
                            self.frame_new_disp.update()
                        else:
                            self.mensagem_confirmacao('O dispositivo não pode ser adicionado')
                            self.apagar_mensagem_confirmacao()
                            self.frame_new_disp.update()                            
                    case "Lâmpada":
                        if Lampada(self.new_name).salvar():
                            self.mensagem_confirmacao('Dispositivo adicionado com sucesso!!')
                            self.parar_execucao()
                            self.frame_new_disp.update()
                            print("Lamp adicionada")
                        else:
                            self.mensagem_confirmacao('O dispositivo não pode ser adicionado')
                            self.apagar_mensagem_confirmacao()
                            self.frame_new_disp.update()
                    case "Televisor":
                        if Televisao(self.new_name).salvar():
                            self.mensagem_confirmacao('Dispositivo adicionado com sucesso!!')
                            self.parar_execucao()
                            self.frame_new_disp.update()
                            print("TV adicionada")
                        else:
                            self.mensagem_confirmacao('O dispositivo não pode ser adicionado')  
                            self.apagar_mensagem_confirmacao()
                            self.frame_new_disp.update()
                            
    def mensagem_confirmacao(self,mensagem) -> None:
        """
        Exibe uma mensagem de confirmação na interface.
        """
        self.texto = ctk.CTkLabel(master=self.frame_new_disp, 
                                  text=mensagem,
                                    font=('League Spartan', 20), 
                                    fg_color='white')
        self.texto.place(x = 75, y = 400)
        self.frame_new_disp.update()
        time.sleep(1)
        
    def apagar_mensagem_confirmacao(self) -> None:
        """
        Apaga a mensagem de confirmação da interface.
        """
        self.texto.destroy()
        
    def parar_execucao(self) -> None:
        """
        Para a execução da interface.
        """
        self.frame_new_disp.destroy()
        
    def executar(self) -> None:
        """
        Executa a interface para adicionar um novo dispositivo.
        """
        self.criaframe()
        self.botao_confirmar()
        