from PIL import Image
import customtkinter as ctk
from src.lampada import Lampada
import time
from src.frame import Frame
from src.automacao import Automacao
from src.planilha import Planilha

class InterfaceLamp:
    """
    Classe que representa a interface gráfica de uma lâmpada.
    """
    def __init__(self, janela:ctk, nome:str, planilha:Planilha) -> None:
        """
        Inicializa a classe InterfaceLamp.
        """
        self.janela = janela
        self.nome = nome
        self.planilha = planilha
        self.lampada = Lampada(self.nome, planilha)
        self.brilho = self.lampada.brilho_atual()
        self.ligado = self.lampada.esta_ligado()

    def criaframe(self) -> None:
        """
        Cria o frame da interface da lâmpada.
        """
        self.frame_lamp = Frame(self.janela, f'{self.nome}', '').frame

    def switch(self) -> None:
        """
        Cria o switch de ligar/desligar da lâmpada.
        """
        off_label = ctk.CTkLabel(self.frame_lamp,
                                 text="OFF",
                                 font=('League Spartan', 30),
                                 fg_color='white',
                                 bg_color='transparent')
        off_label.place(x=100, y=190)
        
        switch = ctk.CTkSwitch(self.frame_lamp,
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
                
        on_label = ctk.CTkLabel(self.frame_lamp,
                                text="ON",
                                font=('League Spartan', 30),
                                fg_color="white",
                                bg_color='transparent')
        on_label.place(x=305, y=190)

        if self.lampada.esta_ligado() == True:
            switch.select()
    
    def slider(self) -> None:
        """
        Cria o slider de controle de brilho da lâmpada.
        """
        self.brilho_label = ctk.CTkLabel(self.frame_lamp,
                                          text=f"Brilho: {self.lampada.brilho_atual()} %",
                                          font=('League Spartan', 30),
                                          bg_color='transparent',
                                          fg_color='#F5F9FC',)
        self.brilho_label.place(x=100, y=330)

        slider_brilho = ctk.CTkSlider(self.frame_lamp,
                                            from_=0, to=100,
                                            command=lambda value: self.atualiza_valor(value),
                                            bg_color='#EDF4F9',
                                            fg_color='gray',
                                            progress_color='#348faa',
                                            button_color='black',
                                            width = 270,
                                            height = 20)
        slider_brilho.set(self.lampada.brilho_atual())
        slider_brilho.place(x=90, y=400)
        
    def botao_excluir(self) -> None:
        """
        Cria o botão de exclusão da lâmpada.
        """
        image = ctk.CTkImage(light_image=Image.open('imagens/excluir.png'), size=(20,20))
        self.botao_excluir = ctk.CTkButton(master=self.frame_lamp, width=170, height=50,
                                             font=('League Spartan bold',17),fg_color='#f5e0df',
                                             corner_radius=0, text='Excluir dispositivo', text_color='black',
                                             command = self.excluir,
                                             image=image
                                             )
        self.botao_excluir.place(x = 140, y = 500)

    def ligar_desligar(self) -> None:
        """
        Liga ou desliga a lâmpada.
        """
        self.lampada.ligar()
    
    def botaoVoltar(self) -> None:
        """
        Cria o botão de exclusão do ar condicionado.
        """
        self.botao_voltar = ctk.CTkButton(master=self.frame_lamp, 
                                           width=170, 
                                           height=50, 
                                           font=('League Spartan bold',17), 
                                           fg_color='#f5e0df', 
                                           corner_radius=0, 
                                           text='Voltar', 
                                           text_color='black', 
                                           command=self.frame_lamp.destroy)
        self.botao_voltar.place(x=140, y=560)

    def atualiza_valor(self, value) -> None:
        """
        Atualiza o valor do brilho da lâmpada.
        """
        self.brilho_label.configure(text=f"Brilho: {int(value)}%")
        self.lampada.mudar_brilho(int(value))
    
    def excluir(self) -> None:
        """
        Exclui a lâmpada da planilha de objetos.
        """
        from interfacedispositivos.InterfaceDispositivos import interfaceDispositivos
        auto = Automacao(self.nome)
        if self.lampada.excluir():
            auto.excluir_auto(1)
            self.mensagem('Dispositivo excluido com sucesso!')
            self.frame_lamp.destroy()
            interfaceDispositivos(self.janela).executar() # Atualiza o frame dos dispositivos.
        
        else:
            self.mensagem('Falha ao excluir o dispositivo')
    
    def mensagem(self, mensagem:str) -> None:
        """
        Cria uma mensagem na tela.
        """
        self.texto = ctk.CTkLabel(master=self.frame_lamp, text=mensagem,
                             font=('League Spartan', 20), fg_color='#CEE2EF')
        self.texto.place(x = 85, y = 620)
        self.frame_lamp.update()
        time.sleep(1)
        

    def executar(self) -> None:
        """
        Executa a interface da lâmpada.
        """
        self.criaframe()
        self.switch()
        self.slider()
        self.botaoVoltar()
        if self.planilha.nome_planilha == 'planilhas/objetos.xlsx':
            self.botao_excluir()



