import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os

class MainMenu(ctk.CTk):
    """
    Classe que representa o menu principal da interface gráfica.

    Attributes:
        bg_image (ImageTk.PhotoImage): Imagem de fundo do menu principal.
        bg_label (tk.Label): Label que exibe a imagem de fundo.
        main_menu_label (ctk.CTkLabel): Label que exibe o título do menu principal.
        button1 (ctk.CTkButton): Botão para abrir o menu de Ar Condicionado.
        button2 (ctk.CTkButton): Botão para abrir o menu de Lâmpadas.
        button3 (ctk.CTkButton): Botão para abrir o menu de Televisões.
        button4 (ctk.CTkButton): Botão para adicionar um novo dispositivo.

    Methods:
        abrir_menu1: Abre o menu de Ar Condicionado.
        abrir_menu2: Abre o menu de Lâmpadas.
        abrir_menu3: Abre o menu de Televisões.
        abrir_menu4: Abre o menu para adicionar um novo dispositivo.
    """
    def __init__(self):
        super().__init__()
        
        self.title("Menu Principal")
        self.geometry("800x600")
        self.configure(bg="#d2e9ec")
        
        back_image = Image.open("imagens/back.png")
        back_image = back_image.resize((800, 600), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(back_image)

        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.main_menu_label = ctk.CTkLabel(self, 
                                            text="Menu Principal", 
                                            font=("Arial Bold", 20),
                                            fg_color="white")
        self.main_menu_label.pack(pady=50)
        
        img1 = ctk.CTkImage(light_image=Image.open("imagens/arcondicionado.png"), 
                           dark_image=Image.open("imagens/arcondicionado.png"),
                           size = (30,30))
        self.button1 = ctk.CTkButton(self , 
                                     text="Ar Condicionado", 
                                     command=self.abrir_menu1, 
                                     width = 150,
                                     height=50,
                                     fg_color="blue",
                                     hover_color= "#4e31ff",
                                     text_color="white",
                                     font = ("arial bold", 18),
                                     corner_radius = 20,
                                     state = "normal",
                                     image=img1,
                                     ).pack(pady=25)
        
        img2 = ctk.CTkImage(light_image=Image.open("imagens/lampada.png"), 
                           dark_image=Image.open("imagens/lampada.png"),
                           size = (30,30))
        self.button2 = ctk.CTkButton(self, 
                                     text="Lâmpadas", 
                                     command=self.abrir_menu2,
                                     width = 150,
                                     height=50,
                                     fg_color="blue",
                                     hover_color= "#4e31ff",
                                     text_color="white",
                                     font = ("arial bold", 18),
                                     corner_radius=20,
                                     state = "normal",
                                     image=img2).pack(pady=25)

        img3 = ctk.CTkImage(light_image=Image.open("imagens/monitor-de-tv.png"), 
                           dark_image=Image.open("imagens/monitor-de-tv.png"),
                           size = (30,30))
        self.button3 = ctk.CTkButton(self, 
                                     text="Televisões", 
                                     command=self.abrir_menu3,
                                     width = 150,
                                     height=50,
                                     fg_color="blue",
                                     hover_color= "#4e31ff",
                                     text_color="white",
                                     font = ("arial bold", 18),
                                     corner_radius=20,
                                     state = "normal",
                                     image=img3).pack(pady=25)
        
        img4 = ctk.CTkImage(light_image=Image.open("imagens/plus.png"), 
                           dark_image=Image.open("imagens/plus.png"),
                           size = (20,20))
        self.button4 = ctk.CTkButton (self, 
                                      text = "Novo dispositivo", 
                                      command = self.abrir_menu4,
                                      width = 150,
                                     height=50,
                                     fg_color="blue",
                                     hover_color= "#4e31ff",
                                     text_color="white",
                                     font = ("arial bold", 18),
                                     corner_radius=20,
                                     state = "normal",
                                     image= img4).pack (pady=25)

    def abrir_menu1(self) -> None:
        """
        Abre o menu de Ar Condicionado.
        """
        MenuAr()
    
    def abrir_menu2(self) -> None:
        """
        Abre o menu de Lâmpadas.
        """
        MenuLampada()

    def abrir_menu3(self) -> None:
        """
        Abre o menu de Televisões.
        """
        MenuTelevisao()

    def abrir_menu4 (self) -> None:
        """
        Abre o menu para adicionar um novo dispositivo.
        """
        MenuAdicionarDispositivo()


class MenuAr(ctk.CTkToplevel):
    """
    Classe que representa o menu de Ar Condicionado.

    Attributes:
        label (ctk.CTkLabel): Label que exibe o título do menu.
        slider_label (ctk.CTkLabel): Label que exibe o texto "Temperatura".
        slider (ctk.CTkSlider): Slider para definir a temperatura.
        slider_value_label (ctk.CTkLabel): Label que exibe o valor da temperatura selecionada.
        back_button (ctk.CTkButton): Botão para retornar ao menu principal.

    Methods:
        definir_temperatura: Atualiza o valor da temperatura selecionada.
    """
    def __init__(self):
        super().__init__()
        
        self.title("Menu do Ar")
        self.geometry("400x240")
        
        self.label = ctk.CTkLabel(self, 
                                  text="Ar condicionados", 
                                  font=("Poppins", 20))
        self.label.pack(pady=10)

        self.slider_label = ctk.CTkLabel(self, 
                                         text="Temperatura")
        self.slider_label.pack(pady=10)

        self.slider = ctk.CTkSlider(self, 
                                    from_=15, to=30, 
                                    command=self.definir_temperatura)
        self.slider.pack(pady=10)

        self.slider_value_label = ctk.CTkLabel(self, 
                                               text="15")
        self.slider_value_label.pack(pady=10)
        
        self.back_button = ctk.CTkButton(self, 
                                         text="Voltar", 
                                         command=self.destroy)
        self.back_button.pack(pady=10)

    def definir_temperatura(self, value) -> None:
        """
        Atualiza o valor da temperatura selecionada.

        Args:
            value (float): Valor da temperatura selecionada.
        """
        self.slider_value_label.configure(text=f"{int(value)}")


class MenuLampada(ctk.CTkToplevel):
    """
    Classe que representa o menu de Lâmpadas.

    Attributes:
        label (ctk.CTkLabel): Label que exibe o título do menu.
        back_button (ctk.CTkButton): Botão para retornar ao menu principal.
    """
    def __init__(self):
        super().__init__()
        
        self.title("Menu das Lâmpadas")
        self.geometry("400x240")
        
        self.label = ctk.CTkLabel(self, 
                                  text="Lâmpadas", 
                                  font=("Poppins", 20))
        self.label.pack(pady=10)
        
        self.back_button = ctk.CTkButton(self, 
                                         text="Voltar", 
                                         command=self.destroy)
        self.back_button.pack(pady=10)

class MenuTelevisao(ctk.CTkToplevel):
    """
    Classe que representa o menu de Televisões.

    Attributes:
        label (ctk.CTkLabel): Label que exibe o título do menu.
        back_button (ctk.CTkButton): Botão para retornar ao menu principal.
    """
    def __init__(self):
        super().__init__()
        
        self.title("Menu dos Televisões")
        self.geometry("400x240")
        
        self.label = ctk.CTkLabel(self, 
                                  text="Televisões", 
                                  font=("Poppins", 20))
        self.label.pack(pady=10)
        
        self.back_button = ctk.CTkButton(self, 
                                         text="Voltar", 
                                         command=self.destroy)
        self.back_button.pack(pady=10)

class MenuAdicionarDispositivo (ctk.CTkToplevel):
    """
    Classe que representa o menu para adicionar um novo dispositivo.

    Attributes:
        label (ctk.CTkLabel): Label que exibe o título do menu.
        opcoes (list): Lista de opções para o tipo de dispositivo.
        option_menu (ctk.CTkOptionMenu): Menu de opções para selecionar o tipo de dispositivo.
        confirm_button (ctk.CTkButton): Botão para confirmar a seleção do tipo de dispositivo.
        back_button (ctk.CTkButton): Botão para retornar ao menu principal.
        entry (None): Campo de entrada de texto para o nome do dispositivo.
        submit_button (None): Botão para submeter o nome do dispositivo.
        novo_nome (None): Variável para armazenar o nome do dispositivo.

    Methods:
        confirmar_dispositivo: Confirma a seleção do tipo de dispositivo.
    """
    def __init__(self):
        super().__init__()
        
        self.title("Novo Dispositivo")
        self.geometry("400x240")
        
        self.label = ctk.CTkLabel(self, 
                                  text="Novo Dispositivo", 
                                  font=("Poppins", 20))
        self.label.pack(pady=10)

        self.opcoes = ["Lâmpada", "Ar Condicionado", "Televisão"]
        self.option_menu = ctk.CTkOptionMenu(self, 
                                             values=self.opcoes)
        self.option_menu.pack(pady=10)

        self.confirm_button = ctk.CTkButton(self, 
                                            text="Confirmar", 
                                            command=self.confirmar_dispositivo)
        self.confirm_button.pack(pady=10)
        
        self.back_button = ctk.CTkButton(self, 
                                         text="Voltar", 
                                         command=self.destroy)
        self.back_button.pack(pady=10)
        
        self.back_button = ctk.CTkButton(self, 
                                         text="Voltar", 
                                         command=self.destroy)
        self.back_button.pack(pady=10)
        self.entry = None
        self.submit_button = None
        self.novo_nome = None

    def confirmar_dispositivo(self):
        """
        Confirma a seleção do tipo de dispositivo.
        """
        escolha = self.option_menu.get()
        print(f"Dispositivo selecionado: {escolha}")
        self.destroy()

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
