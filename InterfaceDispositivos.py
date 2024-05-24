import customtkinter as ctk

class interfaceDispositivos:
    def __init__(self, janela) -> None:
        self.janela = janela
        
    def criaframe(self) -> None:
         self.frame_dispositivos = ctk.CTkFrame(self.janela, width=800, height=500, fg_color='blue')
         #configurar o plano de fundo
         #colocar botões etc
    
    def executar(self) -> None:
        self.criaframe()
        self.frame_dispositivos.place(x = 0, y = 0)
        