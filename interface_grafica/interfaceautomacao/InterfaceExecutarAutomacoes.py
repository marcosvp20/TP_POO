from PIL import Image
import customtkinter as ctk
from src.automacao import Automacao
from src.frame import Frame

class interfaceAutomacao:
    def __init__(self, janela:ctk, nome:str) -> None:
        self.janela = janela
        self.nome = nome

    def criarframe(self) -> None:
        """
        Cria o frame para exibir ações da automação.
        """
        self.frame_automacoes = Frame(self.janela, self.nome, '').frame 
    
    def botaoAtivar(self):
        auto = Automacao(self.nome)
        self.botao_ativar = ctk.CTkButton(master=self.frame_automacoes, 
                                           width=170, 
                                           height=50, 
                                           font=('League Spartan bold',17), 
                                           fg_color='#f5e0df', 
                                           corner_radius=0, 
                                           text='Ativar', 
                                           text_color='black', 
                                           command=auto.executar_automacao)
        self.botao_ativar.place(x=140, y=260)

    def botaoExcluir(self) -> None:
        """
        Cria o botão de exclusão da automação.
        """
        image = ctk.CTkImage(light_image=Image.open('imagens/excluir.png'), size=(20,20))
        auto = Automacao(self.nome)
        self.botao_excluir = ctk.CTkButton(master=self.frame_automacoes, 
                                           width=170, 
                                           height=50, 
                                           font=('League Spartan bold',17), 
                                           fg_color='#f5e0df', 
                                           corner_radius=0, 
                                           text='Excluir automação', 
                                           text_color='black', 
                                           command=auto.excluir_auto,
                                           image=image)
        self.botao_excluir.place(x=140, y=500)

    def executar(self) -> None:
        self.criarframe()
        self.botaoAtivar()
        self.botaoExcluir()