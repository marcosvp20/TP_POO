import customtkinter as ctk
from interface_grafica.menudispositivos.MenuDispositivos import MenuDispositivos
from interface_grafica.menuautomacao.MenuAutomações import MenuAutomacoes
from PIL import Image
from interface_grafica.tela_inicial import TelaInicial

class FrameInferior:
    
    """
        Classe responsável por criar e gerenciar o frame inferior da interface gráfica.
        O frame inferior contém botões para acessar as funcionalidades de Dispositivos e Automações.

        Atributos:
            janela (ctk.CTk): A janela principal da aplicação.
            frame_inferior (ctk.CTkFrame): O frame inferior da interface gráfica.
            botao_dispositivos (ctk.CTkButton): O botão para acessar a interface de Dispositivos.
            botao_automacao (ctk.CTkButton): O botão para acessar a interface de Automações.
    """

    def __init__(self, janela:ctk.CTk) -> None:
        self.janela = janela

        """
        Inicializa a classe FrameInferior.

        Parâmetros:
            janela (ctk.CTk): A janela principal da aplicação.
        """
    
    def criaframe(self) -> None:
        """
        Cria o frame inferior na janela principal.
        """
        self.frame_inferior = ctk.CTkFrame(self.janela, 
                                           width=450, 
                                           height=90, 
                                           fg_color='#e7f0ef', 
                                           corner_radius=0)
        self.frame_inferior.place(x = 0, y = 661.76)
    
    def botaodispositivos(self) -> None:
        """
        Cria o botão de Dispositivos no frame inferior.
        """
        interface_dispositivos = MenuDispositivos(self.janela)
        imagem_dispositivos = ctk.CTkImage(light_image=Image.open('imagens/dispositivos.png'), 
                                           size=(40,40))
        self.botao_dispositivos = ctk.CTkButton(master=self.frame_inferior, 
                                                width=225, 
                                                height=90, 
                                                text='Dispositivos',
                                                fg_color='transparent', 
                                                hover_color='#f3f8fb',
                                                text_color='black',
                                                font=('League Spartan',15), 
                                                image=imagem_dispositivos, 
                                                compound='top',
                                                command= interface_dispositivos.executar)
        self.botao_dispositivos.place(x = 0, y = 0)
    
    def botaoautomacao(self) -> None:
        """
        Cria o botão de Automações no frame inferior.
        """
        interface_automacoes = MenuAutomacoes(self.janela)
        imagem_automacao = ctk.CTkImage(light_image=Image.open('imagens/automacao.png'),
                                        size=(40,40))
        self.botao_automacao = ctk.CTkButton(master=self.frame_inferior, 
                                            width=225, 
                                            height=90, 
                                            text='Automações',
                                            fg_color='transparent', 
                                            hover_color='#f3f8fb',
                                            text_color='black',
                                            font=('League Spartan',15), 
                                            image=imagem_automacao, 
                                            compound='top',
                                            command=interface_automacoes.executar)
        self.botao_automacao.place(x = 225, y = 0)

    def executar(self) -> None:
        """
        Executa a criação do frame inferior e dos botões de Dispositivos e Automações.
        """
        self.criaframe()
        self.botaodispositivos()
        self.botaoautomacao()
        tela_inicial = TelaInicial(self.janela)
        tela_inicial.executar()