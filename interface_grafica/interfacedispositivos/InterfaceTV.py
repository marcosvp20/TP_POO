from PIL import Image
import customtkinter as ctk
from src.planilha import Planilha
from src.televisao import Televisao
import time

class InterfaceTV:
    """
    Classe que representa a interface gráfica de uma televisão.
    """
    def __init__(self, janela:ctk, nome:str) -> None:
        """
        Inicializa a classe InterfaceTV.
        """
        self.janela = janela
        self.nome = nome
        self.planilha = Planilha('objetos.xlsx')
        self.tv = Televisao(self.nome)
        self.tv.volume = self.planilha.retorna_valor(self.nome, 3)
        self.tv.ligado = self.planilha.retorna_valor(self.nome, 4)

    def criaframe(self) -> None:
        """
        Cria o frame da interface da televisão.
        """
        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), 
                          size=(450,750))
        self.frame_tv = ctk.CTkFrame(self.janela, 
                                        width=450, 
                                        height=660,
                                        fg_color= "transparent")
        self.frame_tv.place(x=0, 
                            y=0)
        
        label = ctk.CTkLabel(self.frame_tv, 
                             width=450, 
                             height= 660, 
                             image=bg, 
                             text='')
        
        label.place(x = 0, 
                    y = 0)
        
        self.caixa_de_texto1 = ctk.CTkLabel(self.frame_tv,
                                             text=f'{self.nome}',
                                             font=('League Spartan', 30),
                                             fg_color='white')
        self.caixa_de_texto1.place(x = 30,
                                    y = 40)
        
    def switch(self) -> None:
        """
        Cria o switch de ligar/desligar da televisão.
        """
        off_label = ctk.CTkLabel(self.frame_tv,
                                 text="OFF",
                                 font=('League Spartan', 30),
                                 fg_color='white',
                                 bg_color='transparent')
        off_label.place(x=100, y=190)
        
        switch = ctk.CTkSwitch(self.frame_tv,
                                text="",
                                command=self.ligar_desligar,
                                width=85,
                                height=40,
                                fg_color="gray",
                                progress_color="#348faa",
                                button_color="black",
                                corner_radius=35,
                                bg_color='white',
                                switch_height=40,
                                switch_width=85)
        switch.place(x=183, y=195)
        
        on_label = ctk.CTkLabel(self.frame_tv,
                                text="ON",
                                font=('League Spartan', 30),
                                fg_color='white',
                                bg_color='transparent')
        on_label.place(x=305, y=190)

        if self.planilha.retorna_valor(self.nome, 4):
            switch.select()

    def ligar_desligar(self) -> None:
        """
        Liga ou desliga a televisão.
        """
        self.tv.ligar()


    def botao_excluir(self) -> None:
        """
        Cria o botão de excluir a televisão.
        """
        self.botao_excluir = ctk.CTkButton(master=self.frame_tv, width=170, height=50,
                                        font=('League Spartan bold',17),fg_color='#f5e0df',
                                        corner_radius=0, text='Excluir dispositivo', text_color='black',
                                        command = self.excluir)
        self.botao_excluir.place(x=140, y=560)
    
    def excluir(self) -> None:
        """
        Exclui a televisão.
        """
        if self.planilha.excluir_dispositivo(self.nome):
            self.mensagem('Dispositivo excluído!')
            self.frame_tv.destroy()
            self.janela.update()
        else:
            self.mensagem('Erro ao excluir dispositivo!')   

    def mensagem(self, texto:str) -> None:
        """
        Exibe uma mensagem na tela.
        """
        self.mensagem = ctk.CTkLabel(self.frame_tv, 
                                     text=texto, 
                                     font=('League Spartan', 20), 
                                     fg_color='#d5e8f1')
        self.mensagem.place(x=100, y=620)
        self.frame_tv.update()
        time.sleep(2)

    def executar(self) -> None:
        """
        Executa a interface da televisão.
        """
        self.criaframe()
        self.switch()
        self.botao_excluir()