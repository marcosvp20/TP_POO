import customtkinter as ctk
from InterfaceDispositivos import interfaceDispositivos

class FrameInferior:
    
    def __init__(self, janela) -> None:
        self.janela = janela
    
    def criaframe(self) -> None:
        self.frame_inferior = ctk.CTkFrame(master=self.janela, width=800, height=100, fg_color="#2a2a2a", corner_radius=0)
        self.frame_inferior.place(x = 0, y = 500)

    def botaodispositivos(self) -> None:
        interface_dispositivos = interfaceDispositivos(self.janela)
        self.botao_dispositivos = ctk.CTkButton(master=self.frame_inferior, width=300, height=100, 
                                                corner_radius=35, text='Dispositivos',font= ('Rockwell', 15), 
                                                fg_color='transparent', hover_color='#4e31ff', command=interface_dispositivos.executar)
        self.botao_dispositivos.place(y = 0, x = 50)
    
    def botaoautomacao(self) -> None:
        self.botao_automacao = ctk.CTkButton(master=self.frame_inferior, width=300, height=100, 
                                             corner_radius=35, text='Automação', font= ('Rockwell', 15),
                                             fg_color='transparent', hover_color='#4e31ff')
        self.botao_automacao.place(y = 0, x = 450)
    
    def executar(self) -> None:
        self.criaframe()
        self.botaoautomacao()
        self.botaodispositivos()