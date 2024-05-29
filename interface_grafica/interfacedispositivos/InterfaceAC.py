from PIL import Image
import customtkinter as ctk
from interfacedispositivos.botao_disp import Botao
from src.planilha import Planilha
from src.arcondicionado import ArCondicionado

class InterfaceAC:
    def __init__(self, janela, tipo):
        self.janela = janela
        self.tipo = tipo
        self.planilha = Planilha('objetos.xlsx')
        self.ar = ArCondicionado(nome, "A/C", self.planilha.retorna_valor(nome, 3), self.planilha.retorna_valor(nome, 4))

    def criaframe(self) -> None:

        bg = ctk.CTkImage(light_image=Image.open('imagens/background.png'), 
                          size=(500,750))
        self.frame_ac = ctk.CTkFrame(self.janela, 
                                           width=800, 
                                           height=660,
                                           fg_color= "transparent")
        self.frame_ac.place(x=0, 
                            y=0)
        
        label = ctk.CTkLabel(self.frame_ac, 
                             width=450, 
                             height= 660, 
                             image=bg, 
                             text='')
        
        label.place(x = 0, 
                    y = 0)
        
        self.caixa_de_texto1 = ctk.CTkLabel(self.frame_ac,
                                             text=f'{self.nome}',
                                             font=('League Spartan', 30),
                                             fg_color='white')
        self.caixa_de_texto1.place(x = 10,
                                    y = 60)
        
    def switch(self):
        off_label = ctk.CTkLabel(self.frame_ac, text="OFF")
        off_label.pack(side="left")
        switch = ctk.CTkSwitch(self.frame_ac,
                                text="",
                                command=self.ligar_desligar(),
                                width=100,
                                height=50,
                                fg_color="white",
                                progress_color="#348faa",
                                button_color="#ffffff",
                                button_hover_color="#6A5ACD",
                                border_width=-0.5,
                                corner_radius=10
                                )        
        on_label = ctk.CTkLabel(self.frame_ac, text="ON")
        on_label.pack(side="left")

        if self.planilha.retorna_valor(nome, 4) == True:
            switch.select()
        
        switch.pack()

    def slider(self):
        self.temperatura_label = ctk.CTkLabel(self.frame_ac,
                                          text=f"Temperatura: {self.planilha.retorna_valor(nome, 3)} °C")
        self.temperatura_label.pack(pady=10)

        slider_temperatura = ctk.CTkSlider(self.frame_ac,
                                            from_=16, to=30,
                                            command=self.atualiza_valor())
        slider_temperatura.set(self.planilha.retorna_valor(nome, 3))
        slider_temperatura.pack(pady=10)
        
    def botao_excluir(self):
        self.botao_excluir = ctk.CTkButton(master=self.frame_new_disp, width=170, height=50,
                                             font=('League Spartan bold',17),fg_color='#f5e0df',
                                             corner_radius=0, text='Exlcuir dispositivo', text_color='black',
                                             #command = exlcuir
                                             )
        self.botao_excluir.place(x = 140, y = 320)

    def ligar_desligar(self) -> None:
        if self.planilha.retorna_valor(nome, 4) == True:
            self.ar.desligar()
        elif self.planilha.retorna_valor(nome, 4) == False:
            self.ar.ligar()

    def atualiza_valor(self, value) -> None:
        self.temperatura_label.configure(text=f"Temperatura: {int(value)}° C")
        self.ar.mudar_temperatura(int(value))

    def executar(self):
        self.criaframe()
        self.switch()
        self.slider()


