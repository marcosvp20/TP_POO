import customtkinter as ctk
from frame_inferior import FrameInferior
from PIL import Image

class JanelaPrincipal:
    """
    Classe que representa a janela principal da aplicação ConnecThings.
    Essa janela contém uma imagem de fundo e um frame inferior.
    """

    def __init__(self) -> None:
        """
        Inicializa a janela principal da aplicação ConnecThings.
        Configura a aparência da janela, define o título e o tamanho.
        Cria um rótulo com a imagem de fundo e o frame inferior.
        Executa o loop principal da janela.
        """
        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), 
                          size=(660,750))
        ctk.set_appearance_mode('light') 
        self.janela_principal = ctk.CTk()
        self.janela_principal.title('ConnecThings')
        self.janela_principal.geometry('450x750')
        label = ctk.CTkLabel(self.janela_principal, 
                             width=660, height= 660, 
                             image=bg, 
                             text='')
        label.place(x = 0, y = 0)
        frame_1 = FrameInferior(self.janela_principal)
        frame_1.executar()
        
        self.janela_principal.mainloop()

j = JanelaPrincipal()

    