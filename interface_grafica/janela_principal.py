import customtkinter as ctk
from frame_inferior import FrameInferior
from PIL import Image

class JanelaPrincipal:
    
    def __init__(self) -> None:
        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), size=(450,750))
        ctk.set_appearance_mode('light')
        self.janela_principal = ctk.CTk()
        self.janela_principal.title('ConnecThings')
        self.janela_principal.geometry('450x750')
        label = ctk.CTkLabel(self.janela_principal, width=450, height= 660, image=bg, text='')
        label.place(x = 0, y = 0)
        frame_1 = FrameInferior(self.janela_principal)
        frame_1.executar()

        self.janela_principal.mainloop()

j = JanelaPrincipal()

    