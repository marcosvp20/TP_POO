import customtkinter as ctk
from InterfaceDispositivos import interfaceDispositivos
from interfaceautomacao.interfaceAutomações import interfaceAutomacoes
from PIL import Image

class FrameInferior:
    
    def __init__(self, janela) -> None:
        self.janela = janela
    
    def criaframe(self) -> None:
        self.frame_inferior = ctk.CTkFrame(self.janela, width=450, height=90, fg_color='#e7f0ef', corner_radius=0)
        self.frame_inferior.place(x = 0, y = 661.76)
    
    def botaodispositivos(self) -> None:
        imagem_dispositivos = ctk.CTkImage(light_image=Image.open('imagens/dispositivos.png'), size=(40,40))
        self.botao_dispositivos = ctk.CTkButton(master=self.frame_inferior, width=225, height=90, text='Dispositivos',
                                                fg_color='transparent', hover_color='#f3f8fb',text_color='black',
                                                font=('League Spartan',15), image=imagem_dispositivos, compound='top')
        self.botao_dispositivos.place(x = 0, y = 0)
    
    def botaoautomacao(self) -> None:
        interface_automacoes = interfaceAutomacoes(self.janela)
        imagem_automacao = ctk.CTkImage(light_image=Image.open('imagens/automacao.png'),size=(40,40))
        self.botao_automacao = ctk.CTkButton(master=self.frame_inferior, width=225, height=90, text='Dispositivos',
                                                fg_color='transparent', hover_color='#f3f8fb',text_color='black',
                                                font=('League Spartan',15), image=imagem_automacao, compound='top',
                                                command=interface_automacoes.executar)
        self.botao_automacao.place(x = 225, y = 0)

    def executar(self) -> None:
        self.criaframe()
        self.botaodispositivos()
        self.botaoautomacao()