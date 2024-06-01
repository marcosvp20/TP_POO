from PIL import Image
import customtkinter as ctk
from interfacedispositivos.botao_disp import Botao
from src.planilha import Planilha
from src.arcondicionado import ArCondicionado
import time

class InterfaceAC:
    """
    Classe que representa a interface gráfica de um ar condicionado.
    """
    def __init__(self, janela, nome):
        """
        Inicializa a classe InterfaceAC.
        """
        self.janela = janela
        self.nome = nome
        self.planilha = Planilha('objetos.xlsx')
        self.ar = ArCondicionado(self.nome)
        self.ar.temperatura = self.planilha.retorna_valor(self.nome, 3)
        self.ar.ligado = self.planilha.retorna_valor(self.nome, 4)

    def criaframe(self) -> None:
        """
        Cria o frame da interface do ar condicionado.
        """
        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), size=(450,750))
        self.frame_ac = ctk.CTkFrame(self.janela, 
                                     width=450, 
                                     height=660, 
                                     fg_color="transparent")
        self.frame_ac.place(x=0, y=0)
        
        label = ctk.CTkLabel(self.frame_ac, 
                             width=450, 
                             height= 660, 
                             image=bg, 
                             text='')
        label.place(x=0, y=0)
        
        self.caixa_de_texto1 = ctk.CTkLabel(self.frame_ac, 
                                            text=f'{self.nome}', 
                                            font=('League Spartan', 30), 
                                            fg_color='white')
        self.caixa_de_texto1.place(x=30, y=40)
        
    def switch(self) -> None:
        """
        Cria o switch de ligar/desligar do ar condicionado.
        """
        off_label = ctk.CTkLabel(self.frame_ac, 
                                 text="OFF", 
                                 font=('League Spartan', 30), 
                                 fg_color='white', 
                                 bg_color='transparent')
        off_label.place(x=100, y=190)
        
        switch = ctk.CTkSwitch(self.frame_ac, 
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
                
        on_label = ctk.CTkLabel(self.frame_ac, 
                                text="ON", 
                                font=('League Spartan', 30), 
                                fg_color="white", 
                                bg_color='transparent')
        on_label.place(x=305, y=190)

        if self.planilha.retorna_valor(self.nome, 4) == True:
            switch.select()
    
    def slider(self) -> None:
        """
        Cria o slider de controle de temperatura do ar condicionado.
        """
        self.temperatura_label = ctk.CTkLabel(self.frame_ac, 
                                              text=f"Temperatura: {self.planilha.retorna_valor(self.nome, 3)} °C", 
                                              font=('League Spartan', 30), 
                                              bg_color='transparent', 
                                              fg_color='white',)
        self.temperatura_label.place(x=100, y=330)

        slider_temperatura = ctk.CTkSlider(self.frame_ac, 
                                           from_=16, 
                                           to=30, 
                                           command=lambda value: self.atualiza_valor(value), 
                                           bg_color='transparent', 
                                           fg_color='gray', 
                                           progress_color='#348faa', 
                                           button_color='black', 
                                           width=270, 
                                           height=20)
        slider_temperatura.set(self.planilha.retorna_valor(self.nome, 3))
        slider_temperatura.place(x=90, y=400)
        
    def botao_excluir(self) -> None:
        """
        Cria o botão de exclusão do ar condicionado.
        """
        self.botao_excluir = ctk.CTkButton(master=self.frame_ac, 
                                           width=170, 
                                           height=50, 
                                           font=('League Spartan bold',17), 
                                           fg_color='#f5e0df', 
                                           corner_radius=0, 
                                           text='Excluir dispositivo', 
                                           text_color='black', 
                                           command=self.excluir)
        self.botao_excluir.place(x=140, y=560)

    def ligar_desligar(self) -> None:
        """
        Liga ou desliga o ar condicionado.
        """
        if self.planilha.retorna_valor(self.nome, 4) == True:
            self.ar.desligar()
        elif self.planilha.retorna_valor(self.nome, 4) == False:
            self.ar.ligar()

    def atualiza_valor(self, value) -> None:
        """
        Atualiza o valor da temperatura do ar condicionado.
        """
        self.temperatura_label.configure(text=f"Temperatura: {int(value)}° C")
        self.ar.mudar_temperatura(int(value))
    
    def excluir(self) -> None:
        """
        Exclui o ar condicionado.
        """
        if self.planilha.excluir_dispositivo(self.nome):
            self.mensagem('Dispositivo excluido com sucesso!')
            self.frame_ac.destroy() 
        else:
            self.mensagem('Falha ao excluir o dispositivo')
             
    def mensagem(self, mensagem:str) -> None:
        """
        Exibe uma mensagem na interface do ar condicionado.
        """
        self.texto = ctk.CTkLabel(master=self.frame_ac, 
                                  text=mensagem, 
                                  font=('League Spartan', 20), 
                                  fg_color='#d5e8f1')
        self.texto.place(x=100, y=620)
        self.frame_ac.update()
        time.sleep(1)
        
    def executar(self) -> None:
        """
        Executa a interface do ar condicionado.
        """
        self.criaframe()
        self.switch()
        self.slider()
        self.botao_excluir()

