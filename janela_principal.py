import customtkinter as ctk
from frame_inferior import FrameInferior

class JanelaPrincipal:
    
    def __init__(self) -> None:
        ctk.set_appearance_mode('light')
        self.janela_principal = ctk.CTk(fg_color='white')
        self.janela_principal.title('Main')
        self.janela_principal.geometry('800x600')
        frame_1 = FrameInferior(self.janela_principal)
        frame_1.executar()

        self.janela_principal.mainloop()

j = JanelaPrincipal()

    