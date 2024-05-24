import customtkinter as ctk
from frame_inferior import FrameInferior

class JanelaPrincipal:
    
    def __init__(self) -> None:
        self.janela_principal = ctk.CTk(fg_color='white')
        self.janela_principal.title('Main')
        self.janela_principal.geometry('800x600')
        frame_1 = FrameInferior(self.janela_principal)
        frame_1.executar()
        # self.frameinferior()
        # self.botaodispositivos()
        # self.botaoautomacao()
        self.janela_principal.mainloop()
        
    # def frameinferior(self) -> None:
    #     self.frame_inferior = ctk.CTkFrame(master=self.janela_principal, width=800, height=100, fg_color="#2a2a2a", corner_radius=0)
    #     self.frame_inferior.place(x = 0, y = 500)

    # def botaodispositivos(self) -> None:
    #     self.botao_dispositivos = ctk.CTkButton(master=self.frame_inferior, width=300, height=100, 
    #                                             corner_radius=35, text='Dispositivos',font= ('Rockwell', 15), 
    #                                             fg_color='transparent', hover_color='#4e31ff')
    #     self.botao_dispositivos.place(y = 0, x = 50)
    
    # def botaoautomacao(self) -> None:
    #     self.botao_automacao = ctk.CTkButton(master=self.frame_inferior, width=300, height=100, 
    #                                          corner_radius=35, text='Automação', font= ('Rockwell', 15),
    #                                          fg_color='transparent', hover_color='#4e31ff')
    #     self.botao_automacao.place(y = 0, x = 450)
        

j = JanelaPrincipal()

    