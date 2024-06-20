from interface_grafica.menudispositivos.interfaces_disp.IMenuTV import IMenuTV
from PIL import Image
import customtkinter as ctk
from interface_grafica.src.televisao import Televisao
import time
from interface_grafica.src.frame import Frame
from interface_grafica.src.automacao import Automacao
from interface_grafica.src.planilha import Planilha
from interface_grafica.src.botao import Botao
from interface_grafica.src.slider import Slider
from interface_grafica.src.switch import Switch
class MenuTV(IMenuTV):
    """
    Classe que representa a interface gráfica de uma televisão.
    """
    def __init__(self, janela:ctk, nome:str, planilha:Planilha) -> None:
        """
        Inicializa a classe MenuTV.

        Argumentos:
            janela(ctk): Janela referência à inicialização do menu.
            nome(str): ID do objeto em questão.
            planilha(Planilha): Planilha que contém os dados a serem utilizados.
        """
        self.janela = janela
        self.nome = nome
        self.__planilha = planilha
        self.tv = Televisao(self.nome, planilha)
        self.volume = self.tv.volume_atual()
        self.ligado = self.tv.esta_ligado()
        self.canal = self.tv.canal_atual()

    def criaframe(self) -> None:
        """
        Cria o frame da interface da televisão.
        """
        self.__frame =  Frame(self.janela, f'{self.nome}', '')
        self.__frame_tv = self.__frame.retorna_frame()

    def switch(self) -> None:
        """
        Cria o switch de ligar/desligar da televisão.
        """
        off_label = ctk.CTkLabel(self.__frame_tv,
                                 text="OFF",
                                 font=('League Spartan', 30),
                                 fg_color='white',
                                 bg_color='transparent')
        off_label.place(x=100, y=190)

        self.__switch = Switch(self.__frame_tv, self.ligar_desligar,
                               183, 195)
        
        on_label = ctk.CTkLabel(self.__frame_tv,
                                text="ON",
                                font=('League Spartan', 30),
                                fg_color='white',
                                bg_color='transparent')
        on_label.place(x=305, y=190)

        if self.tv.esta_ligado():
            self.__switch.switch.select()

    def ligar_desligar(self) -> None:
        """
        Liga ou desliga a televisão.
        """
        self.tv.ligar()
    
    def slider(self) -> None:
        """
        Cria o slider de controle do volume da tv.
        """
        self.label_volume = ctk.CTkLabel(self.__frame_tv,
                                          text=f"Volume: {self.tv.volume_atual()} %",
                                          font=('League Spartan', 30),
                                          bg_color='transparent',
                                          fg_color='#F0F6FA',)
        self.label_volume.place(x=140, y=380)
        
        self.__slider_volume = Slider(frame=self.__frame_tv, inicio=0, fim=100,
                                      comando=self.atualiza_valor, posicao_atual=self.tv.volume_atual,
                                      posx=90, posy=450)

    def botaoExcluir(self) -> None:
        """
        Cria o botão de excluir a televisão.
        """
        image = ctk.CTkImage(light_image=Image.open('imagens/excluir.png'), size=(20,20))
        self.botao_excluir = Botao(janela=self.__frame_tv, posx=140, posy=560, imagem=image,
                                   comando=self.excluir, texto='Excluir dispositivo')
        self.botao_excluir.botao_menor('#f5e0df')
    
    def botaoVoltar(self) -> None:
        """
        Cria o botão de exclusão do ar condicionado.
        """
        self.botao_voltar = Botao(self.__frame_tv, posx=140, posy=500, texto='Voltar',
                                  comando=self.__frame.destroy)
        self.botao_voltar.botao_menor('white')
    
    def botoes_mudar_canal(self) -> None:
        """
        Cria os botões de alteração de canal da TV.
        """
        imagem_mais = ctk.CTkImage(light_image=Image.open('imagens/adicionar.png'), size=(30,30))
        imagem_menos = ctk.CTkImage(light_image=Image.open('imagens/menos.png'), size=(30,30))
        
        self.botao_menos = ctk.CTkButton(master=self.__frame_tv, width=60, height=30,
                                        image=imagem_menos, corner_radius=30,font=('League Spartan',30),
                                        bg_color='#F8FBFD', fg_color='#F3F8FB', text=None, hover_color='light gray',
                                        border_width=4, border_color='#348FAA', command=self.click_botao_menos)
        self.botao_menos.place(x = 70, y = 320)
    
        self.botao_mais = ctk.CTkButton(master=self.__frame_tv, width=60, height=30,
                                        image=imagem_mais, corner_radius=30,font=('League Spartan',30),
                                        bg_color='#F8FBFD', fg_color='#F3F8FB', text=None, hover_color='light gray',
                                        border_width=4, border_color='#348FAA', command=self.click_botao_mais)
        self.botao_mais.place(x = 325, y = 320)
        
        self.label_ch = ctk.CTkLabel(master=self.__frame_tv, text=f'CH {self.tv.canal_atual()}', font=('League Spartan bold',30),
                                     bg_color='#F8FBFD')
        self.label_ch.place(x = 200, y = 315)
        
    def click_botao_mais(self) -> None:
        """
        Passa para o próximo canal.
        """
        canal = self.tv.canal_atual()
        canal += 1
        self.alterar_canal(canal)
    
    def click_botao_menos(self) -> None:
        """
        Passa para o canal anterior.
        """
        canal = self.tv.canal_atual()
        if canal == 1:
            return
        else:
            canal -= 1
        self.alterar_canal(canal)
        
    def alterar_canal(self, canal:int)->None:
        """
        Muda o canal da TV para um especificado.

        Argumentos:
            canal(int): Número do canal.
        """
        self.tv.mudar_canal(canal)
        self.label_ch.configure(text = f'CH {int(canal)}')
    
    def excluir(self) -> None:
        """
        Exclui a televisão.
        """
        from interface_grafica.menudispositivos.MenuDispositivos import MenuDispositivos
        auto = Automacao(self.nome)

        if self.tv.excluir():
            auto.excluir_auto(1)
            self.mensagem('Dispositivo excluído com sucesso!')
            self.__frame.destroy()
            MenuDispositivos(self.janela).executar() # Atualiza o frame dos dispositivos.
        else:
            self.mensagem('Erro ao excluir dispositivo!')   

    def mensagem(self, texto:str) -> None:
        """
        Exibe uma mensagem na tela.

        Argumentos:
            texto(str): Texto a ser exibido.
        """
        self.mensagem = ctk.CTkLabel(self.__frame_tv, 
                                     text=texto, 
                                     font=('League Spartan', 20), 
                                     fg_color='#CEE2EF')
        self.mensagem.place(x=85, y=620)
        self.__frame_tv.update()
        time.sleep(1)
        
    def atualiza_valor(self, value:int) -> None:
        """
        Atualiza o valor do volume da tv.

        Argumentos:
            value: Valor atualizado.
        """
        self.label_volume.configure(text=f"Volume: {int(value)}%")
        self.tv.mudar_volume(int(value))

    def botaoConfirmar(self) -> None:
        """
        Cria o botão de seleção do ar condicionado para adicionar à uma automação.
        """
        image = ctk.CTkImage(light_image=Image.open('imagens/check.png'), size=(20,20))
        
        self.botao_confirmar = Botao(janela=self.__frame_tv, posx=140, posy=560, imagem=image,
                                   comando=self.confirmar, texto='Confirmar')
        self.botao_confirmar.botao_menor('white')

    def confirmar(self) -> None:
        """
        Seleciona o dispositivo para ser adicionado à uma automação.
        """
        self.__planilha.selecionar(self.nome)
        self.mensagem('               Alterações salvas')
        self.mensagem.destroy()
        
    def executar(self) -> None:
        """
        Executa a interface da televisão.
        """
        self.criaframe()
        self.switch()
        self.slider()
        self.botoes_mudar_canal()
        self.botaoVoltar()
        if self.__planilha.nome_planilha == 'planilhas/objetos.xlsx':
            self.botaoExcluir()
        elif self.__planilha.nome_planilha == 'planilhas/automacoestemp.xlsx':
            self.botaoConfirmar()