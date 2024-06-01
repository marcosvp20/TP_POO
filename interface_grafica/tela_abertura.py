import customtkinter as ctk
import time
from PIL import Image

class TelaAbertura:
    def __init__(self, janela:ctk) -> None:
        self.janela = janela
    
    def cria_frame(self) -> None:
        self.frame = ctk.CTkFrame(master=self.janela,
                                  width=450,
                                  height=750,
                                  fg_color='transparent')
        self.frame.place(x= 0, y = 0)
        
    def imagem(self) -> None:
        imagem = ctk.CTkImage(Image.open('imagens/inicio.png'),size=(450,750))
        self.label = ctk.CTkLabel(master=self.frame,
                             width=450,
                             height=750,
                             image=imagem,
                             text='')
        self.label.place(x = 0, y = 0)
    
    def apagar(self) -> None:
        self.frame.destroy()
        
    def executar(self) -> None:
        self.cria_frame()
        self.imagem()
        time.sleep(1)

# j = ctk.CTk()
# j.geometry('450x750')
# t = TelaAbertura(j)
# t.executar()
# j.mainloop()
