import customtkinter as ctk
from PIL import Image
from interfaceautomacao.botao import Botao

class interfaceAutomacoes:
    def __init__(self, janela) -> None:
        self.janela = janela
    
    def criarframe(self) -> None:
        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), size=(450,750))
        self.frame_automacoes = ctk.CTkFrame(self.janela, width=450, height=640, fg_color='transparent')
        self.frame_automacoes.place(x = 0, y = 0)
        label = ctk.CTkLabel(self.frame_automacoes, width=450, height= 660, image=bg, text='')
        label.place(x = 0, y = 0)
    
    def botaoadicionar(self) -> None:
        imagem = ctk.CTkImage(light_image= Image.open('imagens/plus.png'),size=(25,25))
        botao_adicionar = Botao(janela=self.frame_automacoes, posx=42, posy=184, texto='Adicionar\nAutomação', imagem=imagem)
    
    # def texto1(self) -> None:
    #     texto_1 = ctk.CTkLabel(self.frame_automacoes, width=279, height=33.6, text='ConnecThings', font=('League Spartan bold',15), 
    #                            fg_color= 'transparent')
    #     texto_1.place(x = 35, y = 20)
   
    def executar(self) -> None:
        self.criarframe()
        self.botaoadicionar()
        # self.texto1()