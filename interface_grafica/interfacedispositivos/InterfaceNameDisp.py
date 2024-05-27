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
    def __init__(self, janela, tipo) -> None:
        self.janela = janela
        self.tipo = tipo
        self.planilha = Planilha('objetos.xlsx')

        
    def criaframe(self) -> None:
        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), 
                          size=(450,750))
        self.frame_new_disp = ctk.CTkFrame(self.janela, 
                                           width=800, 
                                           height=500,
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
                                             text='Qual dispositivo será o nome',
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
                                 width=180, 
                                 font=('League Spartan', 20),
                                 placeholder_text="Nome do dispositivo",
                                 placeholder_text_color="gray")
        self.txtbox_name_disp.place(x=135,   
                            y=200)
        
    def botao_confirmar (self):
        imagem = ctk.CTkImage(light_image= Image.open('imagens/plus.png'),size=(25,25))
        self.botao_adicionar = Botao(janela=self.frame_new_disp, 
                                    posx=135, 
                                    posy=250, 
                                    texto='Confirmar', 
                                    imagem=imagem,
                                    comando=self.adicionar)
        
    def adicionar(self):
        self.frame_new_disp.update()
        if self.tipo: # Garantir que não está vazio
            self.new_name = self.txtbox_name_disp.get().strip()
            print(self.new_name)
            if self.new_name:
                match(self.tipo):
                    case "A/C":
                        if ArCondicionado(self.new_name).salvar():
                            print("AC adicionado")
                            self.mensagem_confirmacao('Dispositivo adicionado com sucesso!!')
                            self.apagar_mensagem_confirmacao()
                            self.frame_new_disp.update()
                        else:
                            self.mensagem_confirmacao('O número máximo de dispositivos\n foi atingido')
                            self.apagar_mensagem_confirmacao()
                            self.frame_new_disp.update()                            
                    case "Lâmpada":
                        if Lampada(self.new_name).salvar():
                            self.mensagem_confirmacao('Dispositivo adicionado com sucesso!!')
                            self.apagar_mensagem_confirmacao()
                            self.frame_new_disp.update()
                            print("Lamp adicionada")
                        else:
                            self.mensagem_confirmacao('O número máximo de dispositivos\n foi atingido')
                            self.apagar_mensagem_confirmacao()
                            self.frame_new_disp.update()
                    case "Televisor":
                        if Televisao(self.new_name).salvar():
                            self.mensagem_confirmacao('Dispositivo adicionado com sucesso!!')
                            self.apagar_mensagem_confirmacao()
                            self.frame_new_disp.update()
                            print("TV adicionada")
                        else:
                            self.mensagem_confirmacao('O número máximo de dispositivos\n foi atingido')  
                            self.apagar_mensagem_confirmacao()
                            self.frame_new_disp.update()
                            
    def mensagem_confirmacao(self,mensagem) -> None:
        self.texto = ctk.CTkLabel(master=self.frame_new_disp, text=mensagem,
                             font=('League Spartan', 20), fg_color='white')
        self.texto.place(x = 75, y = 350)
        self.frame_new_disp.update()
        time.sleep(1)
        
    def apagar_mensagem_confirmacao(self):
        self.texto.destroy()
        
    def parar_execucao(self) -> None:
        self.frame_new_disp.destroy()
        


    def executar(self) -> None:
        self.criaframe()
        self.botao_confirmar()
        