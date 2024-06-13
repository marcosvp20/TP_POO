from PIL import Image
import customtkinter as ctk
from src.televisao import Televisao
import time
from src.frame import Frame
from src.automacao import Automacao
from src.planilha import Planilha

class InterfaceTV:
    """
    Classe que representa a interface gráfica de uma televisão.
    """
    def __init__(self, janela:ctk, nome:str, planilha:Planilha) -> None:
        """
        Inicializa a classe InterfaceTV.
        """
        self.janela = janela
        self.nome = nome
        self.planilha = planilha
        self.tv = Televisao(self.nome, planilha)
        self.volume = self.tv.volume_atual()
        self.ligado = self.tv.esta_ligado()
        self.canal = self.tv.canal_atual()

    def criaframe(self) -> None:
        """
        Cria o frame da interface da televisão.
        """
        self.frame_tv = Frame(self.janela, f'{self.nome}', '').frame

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

        if self.tv.esta_ligado():
            switch.select()

    def ligar_desligar(self) -> None:
        """
        Liga ou desliga a televisão.
        """
        self.tv.ligar()
    
    def slider(self) -> None:
        """
        Cria o slider de controle do volume da tv.
        """
        self.label_volume = ctk.CTkLabel(self.frame_tv,
                                          text=f"Volume: {self.tv.volume_atual()} %",
                                          font=('League Spartan', 30),
                                          bg_color='transparent',
                                          fg_color='#E5F0F7',)
        self.label_volume.place(x=140, y=380)

        slider_volume = ctk.CTkSlider(self.frame_tv,
                                            from_=0, to=100,
                                            command=lambda value: self.atualiza_valor(value),
                                            bg_color='#DFECF4',
                                            fg_color='gray',
                                            progress_color='#348faa',
                                            button_color='black',
                                            width = 270,
                                            height = 20)
        slider_volume.set(self.tv.volume_atual())
        slider_volume.place(x=90, y=450)


    def botaoExcluir(self) -> None:
        """
        Cria o botão de excluir a televisão.
        """
        image = ctk.CTkImage(light_image=Image.open('imagens/excluir.png'), size=(20,20))
        self.botao_excluir = ctk.CTkButton(master=self.frame_tv, width=170, height=50,
                                        font=('League Spartan bold',17),fg_color='#f5e0df',
                                        corner_radius=0, text='Excluir dispositivo', text_color='black',
                                        command = self.excluir,
                                        image=image)
        self.botao_excluir.place(x=140, y=500)
    
    def botaoVoltar(self) -> None:
        """
        Cria o botão de exclusão do ar condicionado.
        """
        self.botao_voltar = ctk.CTkButton(master=self.frame_tv, 
                                           width=170, 
                                           height=50, 
                                           font=('League Spartan bold',17), 
                                           fg_color='#f5e0df', 
                                           corner_radius=0, 
                                           text='Voltar', 
                                           text_color='black', 
                                           command=self.frame_tv.destroy)
        self.botao_voltar.place(x=140, y=560)
    
    def botoes_mudar_canal(self):
        imagem_mais = ctk.CTkImage(light_image=Image.open('imagens/adicionar.png'), size=(30,30))
        imagem_menos = ctk.CTkImage(light_image=Image.open('imagens/menos.png'), size=(30,30))
        
        self.botao_menos = ctk.CTkButton(master=self.frame_tv, width=60, height=30,
                                        image=imagem_menos, corner_radius=30,font=('League Spartan',30),
                                        bg_color='#F8FBFD', fg_color='#F3F8FB', text=None, hover_color='light gray',
                                        border_width=4, border_color='#348FAA', command=self.click_botao_menos)
        self.botao_menos.place(x = 70, y = 320)
    
        self.botao_mais = ctk.CTkButton(master=self.frame_tv, width=60, height=30,
                                        image=imagem_mais, corner_radius=30,font=('League Spartan',30),
                                        bg_color='#F8FBFD', fg_color='#F3F8FB', text=None, hover_color='light gray',
                                        border_width=4, border_color='#348FAA', command=self.click_botao_mais)
        self.botao_mais.place(x = 325, y = 320)
        
        self.label_ch = ctk.CTkLabel(master=self.frame_tv, text=f'CH {self.tv.canal_atual()}', font=('League Spartan bold',30),
                                     bg_color='#F8FBFD')
        self.label_ch.place(x = 200, y = 315)
        
    def click_botao_mais(self) -> None:
        canal = self.tv.canal_atual()
        canal += 1
        self.alterar_canal(canal)
    
    def click_botao_menos(self) -> None:
        canal = self.tv.canal_atual()
        if canal == 1:
            return
        else:
            canal -= 1
        self.alterar_canal(canal)
        
    def alterar_canal(self, canal:int):
        self.tv.mudar_canal(canal)
        self.label_ch.configure(text = f'CH {int(canal)}')
    
    def excluir(self) -> None:
        """
        Exclui a televisão.
        """
        from interfacedispositivos.InterfaceDispositivos import interfaceDispositivos
        auto = Automacao(self.nome)

        if self.tv.excluir():
            print(self.nome)
            auto.excluir_auto(1)
            self.mensagem('Dispositivo excluído com sucesso!')
            self.frame_tv.destroy()
            interfaceDispositivos(self.janela).executar() # Atualiza o frame dos dispositivos.
        else:
            self.mensagem('Erro ao excluir dispositivo!')   

    def mensagem(self, texto:str) -> None:
        """
        Exibe uma mensagem na tela.
        """
        self.mensagem = ctk.CTkLabel(self.frame_tv, 
                                     text=texto, 
                                     font=('League Spartan', 20), 
                                     fg_color='#CEE2EF')
        self.mensagem.place(x=85, y=620)
        self.frame_tv.update()
        time.sleep(2)
        
    def atualiza_valor(self, value) -> None:
        """
        Atualiza o valor do volume da tv.
        """
        self.label_volume.configure(text=f"Volume: {int(value)}%")
        self.tv.mudar_volume(int(value))

    def executar(self) -> None:
        """
        Executa a interface da televisão.
        """
        self.criaframe()
        self.switch()
        self.slider()
        self.botoes_mudar_canal()
        self.botaoVoltar()
        if self.planilha.nome_planilha == 'planilhas/objetos.xlsx':
            self.botaoExcluir()