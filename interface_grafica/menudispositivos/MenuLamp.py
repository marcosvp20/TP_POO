from interface_grafica.menudispositivos.interfaces_disp.IMenuLamp import IMenuLamp
from PIL import Image
import customtkinter as ctk
from interface_grafica.src.lampada import Lampada
import time
from interface_grafica.src.frame import Frame
from interface_grafica.src.automacao import Automacao
from interface_grafica.src.planilha import Planilha
from interface_grafica.src.botao import Botao
from interface_grafica.src.slider import Slider

class MenuLamp(IMenuLamp):
    """
    Classe que representa a interface gráfica de uma lâmpada.
    """
    def __init__(self, janela:ctk, nome:str, planilha:Planilha) -> None:
        """
        Inicializa a classe MenuLamp.

        Argumentos:
            janela(ctk): Janela referência à inicialização do menu.
            nome(str): ID do objeto em questão.
            planilha(Planilha): Planilha que contém os dados a serem utilizados.
        """
        self.janela = janela
        self.nome = nome
        self.__planilha = planilha
        self.lampada = Lampada(self.nome, planilha)
        self.brilho = self.lampada.brilho_atual()
        self.ligado = self.lampada.esta_ligado()

    def criaframe(self) -> None:
        """
        Cria o frame da interface da lâmpada.
        """
        self.__frame = Frame(self.janela, f'{self.nome}', '')
        self.__frame_lamp = self.__frame.retorna_frame()

    def switch(self) -> None:
        """
        Cria o switch de ligar/desligar da lâmpada.
        """
        off_label = ctk.CTkLabel(self.__frame_lamp,
                                 text="OFF",
                                 font=('League Spartan', 30),
                                 fg_color='white',
                                 bg_color='transparent')
        off_label.place(x=100, y=190)
        
        switch = ctk.CTkSwitch(self.__frame_lamp,
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
                
        on_label = ctk.CTkLabel(self.__frame_lamp,
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
        self.brilho_label = ctk.CTkLabel(self.__frame_lamp,
                                          text=f"Brilho: {self.lampada.brilho_atual()} %",
                                          font=('League Spartan', 30),
                                          bg_color='transparent',
                                          fg_color='#F5F9FC',)
        self.brilho_label.place(x=100, y=330)
        
        self.__slider_brilho = Slider(frame=self.__frame_lamp, inicio=0, fim=100,
                                      comando=self.atualiza_valor, posicao_atual=self.lampada.brilho_atual,
                                      posx=90, posy=400)

        
    def botao_excluir(self) -> None:
        """
        Cria o botão de exclusão da lâmpada.
        """
        image = ctk.CTkImage(light_image=Image.open('imagens/excluir.png'), size=(20,20))
        self.botaoExcluir = Botao(self.__frame_lamp, posx=140, posy=560,
                                  texto='Excluir dispositivo',imagem=image, comando=self.excluir)
        self.botaoExcluir.botao_menor('#f5e0df')

    def ligar_desligar(self) -> None:
        """
        Liga ou desliga a lâmpada.
        """
        self.lampada.ligar()
    
    def botaoVoltar(self) -> None:
        """
        Cria o botão de exclusão do ar condicionado.
        """
        
        self.botao_voltar = Botao(self.__frame_lamp, posx=140, posy=500, texto='Voltar',
                                  comando=self.__frame.destroy)
        self.botao_voltar.botao_menor('white')
        
    def atualiza_valor(self, value) -> None:
        """
        Atualiza o valor do brilho da lâmpada.

        Argumentos:
            value: Valor atualizado.
        """
        self.brilho_label.configure(text=f"Brilho: {int(value)}%")
        self.lampada.mudar_brilho(int(value))
    
    def excluir(self) -> None:
        """
        Exclui a lâmpada da planilha de objetos.
        """
        from interface_grafica.menudispositivos.MenuDispositivos import MenuDispositivos

        auto = Automacao(self.nome)
        if self.lampada.excluir():
            auto.excluir_auto(1)
            self.mensagem('Dispositivo excluido com sucesso!')
            self.__frame.destroy()
            MenuDispositivos(self.janela).executar() # Atualiza o frame dos dispositivos.
        else:
            self.mensagem('Falha ao excluir o dispositivo')
    
    def mensagem(self, mensagem:str) -> None:
        """
        Cria uma mensagem na tela.

        Argumentos:
            mensagem(str): Texto a ser exibido.
        """
        self.texto = ctk.CTkLabel(master=self.__frame_lamp, text=mensagem,
                             font=('League Spartan', 20), fg_color='#CEE2EF')
        self.texto.place(x = 85, y = 620)
        self.__frame_lamp.update()
        time.sleep(1)

    def botaoConfirmar(self) -> None:
        """
        Cria o botão de seleção do ar condicionado para adicionar à uma automação.
        """
        image = ctk.CTkImage(light_image=Image.open('imagens/check.png'), size=(20,20))
        
        self.botao_confirmar = Botao(janela=self.__frame_lamp, posx=140, posy=560, imagem=image,
                                   comando=self.confirmar, texto='Confirmar')
        self.botao_confirmar.botao_menor('white')

    def confirmar(self) -> None:
        """
        Seleciona o dispositivo para ser adicionado à uma automação.
        """
        self.__planilha.selecionar(self.nome)
        self.mensagem('               Alterações salvas')
        self.texto.destroy()

    def executar(self) -> None:
        """
        Executa a interface da lâmpada.
        """
        self.criaframe()
        self.switch()
        self.slider()
        self.botaoVoltar()
        if self.__planilha.nome_planilha == 'planilhas/objetos.xlsx':
            self.botao_excluir()
        elif self.__planilha.nome_planilha == 'planilhas/automacoestemp.xlsx':
            self.botaoConfirmar()



