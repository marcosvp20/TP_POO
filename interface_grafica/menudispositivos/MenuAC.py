from interface_grafica.menudispositivos.interfaces_disp.IMenuAC import IMenuAC
from PIL import Image
import customtkinter as ctk
from interface_grafica.src.arcondicionado import ArCondicionado
import time
from interface_grafica.src.frame import Frame
from interface_grafica.src.automacao import Automacao
from interface_grafica.src.planilha import Planilha
from interface_grafica.src.botao import Botao
from interface_grafica.src.slider import Slider

class MenuAC(IMenuAC):
    """
    Classe que representa a interface gráfica de um ar condicionado.
    """
    def __init__(self, janela:ctk, nome:str, planilha:Planilha):
        """
        Inicializa a classe MenuAC.

        Argumentos:
            janela(ctk): Janela referência à inicialização do menu.
            nome(str): ID do objeto em questão.
            planilha(Planilha): Planilha que contém os dados a serem utilizados.
        """
        self.janela = janela
        self.nome = nome
        self.__planilha = planilha
        self.ar = ArCondicionado(self.nome, planilha)
        self.ar.temperatura = self.ar.temperatura_atual()
        self.ar.ligado = self.ar.esta_ligado()

    def criaframe(self) -> None:
        """
        Cria o frame da interface do ar condicionado.
        """
        self.__frame = Frame(self.janela, f'{self.nome}', '')
        self.__frame_ac = self.__frame.retorna_frame()
        
    def switch(self) -> None:
        """
        Cria o switch de ligar/desligar do ar condicionado.
        """
        off_label = ctk.CTkLabel(self.__frame_ac, 
                                 text="OFF", 
                                 font=('League Spartan', 30), 
                                 fg_color='white', 
                                 bg_color='transparent')
        off_label.place(x=100, y=190)
        
        switch = ctk.CTkSwitch(self.__frame_ac, 
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
                
        on_label = ctk.CTkLabel(self.__frame_ac, 
                                text="ON", 
                                font=('League Spartan', 30), 
                                fg_color="white", 
                                bg_color='transparent')
        on_label.place(x=305, y=190)

        if self.ar.esta_ligado() == True:
            switch.select()
    
    def slider(self) -> None:
        """
        Cria o slider de controle de temperatura do ar condicionado.
        """
        self.temperatura_label = ctk.CTkLabel(self.__frame_ac, 
                                              text=f"Temperatura: {self.ar.temperatura_atual()} °C", 
                                              font=('League Spartan', 30), 
                                              bg_color='#F5F9FC', 
                                              fg_color='white',)
        self.temperatura_label.place(x=100, y=330)
        
        self.__slider_temperatura = Slider(frame=self.__frame_ac, inicio=16, fim=30,
                                           comando=self.atualiza_valor, posicao_atual=self.ar.temperatura_atual,
                                           posx=90, posy=400)

    def botaoExcluir(self) -> None:
        """
        Cria o botão de exclusão do ar condicionado.
        """
        image = ctk.CTkImage(light_image=Image.open('imagens/excluir.png'), size=(20,20))
        
        self.botao_excluir = Botao(janela=self.__frame_ac, posx=140, posy=500, imagem=image,
                                   comando=self.excluir, texto='Excluir dispositivo')
        self.botao_excluir.botao_menor('#f5e0df')

        
    def botaoVoltar(self) -> None:
        """
        Cria o botão de voltar ao menu anterior.
        """
        self.botao_voltar = Botao(self.__frame_ac, posx=140, posy=560, texto='Voltar',
                                  comando=self.__frame.destroy)
        self.botao_voltar.botao_menor('#f5e0df')

    def ligar_desligar(self) -> None:
        """
        Liga ou desliga o ar condicionado.
        """
        if self.ar.esta_ligado() == True:
            self.ar.desligar()
        elif self.ar.esta_ligado() == False:
            self.ar.ligar()

    def atualiza_valor(self, value) -> None:
        """
        Atualiza o valor da temperatura do ar condicionado.

        Argumentos:
            value: Valor atualizado.
        """
        self.temperatura_label.configure(text=f"Temperatura: {int(value)}° C")
        self.ar.mudar_temperatura(int(value))
    
    def excluir(self) -> None:
        """
        Exclui o ar condicionado.
        """
        from interface_grafica.menudispositivos.MenuDispositivos import MenuDispositivos

        auto = Automacao(self.nome)
        if self.ar.excluir():
            auto.excluir_auto(1)
            self.mensagem('Dispositivo excluido com sucesso!')
            self.__frame.destroy()
            MenuDispositivos(self.janela).executar() # Atualiza o frame dos dispositivos.
        else:
            self.mensagem('Falha ao excluir o dispositivo')
             
    def mensagem(self, mensagem:str) -> None:
        """
        Exibe uma mensagem na interface do ar condicionado.

        Argumentos: 
            mensagem(str): Texto a ser exibido.
        """
        self.mensagem = ctk.CTkLabel(master=self.__frame_ac, 
                                  text=mensagem, 
                                  font=('League Spartan', 20), 
                                  fg_color='#CEE2EF',
                                  anchor='center')
        self.mensagem.place(x=85, y=620)
        self.__frame_ac.update()
        time.sleep(1)

    def botaoConfirmar(self) -> None:
        """
        Cria o botão de seleção do ar condicionado para adicionar à uma automação.
        """
        image = ctk.CTkImage(light_image=Image.open('imagens/check.png'), size=(20,20))
        
        self.botao_confirmar = Botao(janela=self.__frame_ac, posx=140, posy=500, imagem=image,
                                   comando=self.confirmar, texto='Confirmar')
        self.botao_confirmar.botao_menor('#f5e0df')

    def confirmar(self) -> None:
        """
        Seleciona o dispositivo para ser adicionado à uma automação.
        """
        self.__planilha.selecionar(self.nome)
        self.mensagem('               Alterações salvas')
        self.mensagem.destroy()
        
    def executar(self) -> None:
        """
        Executa a interface do ar condicionado.
        """
        self.criaframe()
        self.switch()
        self.slider()
        self.botaoVoltar()
        if self.__planilha.nome_planilha == 'planilhas/objetos.xlsx':
            self.botaoExcluir()
        elif self.__planilha.nome_planilha == 'planilhas/automacoestemp.xlsx':
            self.botaoConfirmar()
        

