import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os

class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Definição da janela
        self.title("Menu Principal")
        self.geometry("800x600")
        self.configure(bg="#d2e9ec")
        
        back_image = Image.open("imagens/back.png")
        back_image = back_image.resize((800, 600), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(back_image)

        # Configura a imagem de fundo
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        #definição de etiquetas
        self.main_menu_label = ctk.CTkLabel(self, 
                                            text="Menu Principal", 
                                            font=("Arial Bold", 20),
                                            fg_color="white")
        self.main_menu_label.pack(pady=50)
        
        # frame1 = ctk.CTkFrame(self, 
        #                       width=500, 
        #                       height=500, 
        #                       corner_radius=30,
        #                       bg_color= "white")
        # frame1.pack(pady=10)
        #botão do menu dos Ar Condicionado
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
        
        #botão do menu de lâmpadas
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

        #botão do menu de televisões
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
        
        #botão adicionar dispositivo
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
        MenuAr()
    
    def abrir_menu2(self) -> None:
        MenuLampada()

    def abrir_menu3(self) -> None:
        MenuTelevisao()

    def abrir_menu4 (self) -> None:
        MenuAdicionarDispositivo()


class MenuAr(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        
        #definição da janela
        self.title("Menu do Ar")
        self.geometry("400x240")
        
        #definição de etiquetas
        self.label = ctk.CTkLabel(self, 
                                  text="Ar condicionados", 
                                  font=("Poppins", 20))
        self.label.pack(pady=10)

        #criação de um slider
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
        
        #botão retornar
        self.back_button = ctk.CTkButton(self, 
                                         text="Voltar", 
                                         command=self.destroy)
        self.back_button.pack(pady=10)

    #funcao que atualiza o valor colocado no slider
    def definir_temperatura(self, value) -> None:
        self.slider_value_label.configure(text=f"{int(value)}")


class MenuLampada(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        
        #definição da janela
        self.title("Menu das Lâmpadas")
        self.geometry("400x240")
        
        #definição de etiquetas
        self.label = ctk.CTkLabel(self, 
                                  text="Lâmpadas", 
                                  font=("Poppins", 20))
        self.label.pack(pady=10)
        
        #botão retornar
        self.back_button = ctk.CTkButton(self, 
                                         text="Voltar", 
                                         command=self.destroy)
        self.back_button.pack(pady=10)

class MenuTelevisao(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        
        #definição da janela
        self.title("Menu dos Televisões")
        self.geometry("400x240")
        
        #definição de etiquetas
        self.label = ctk.CTkLabel(self, 
                                  text="Televisões", 
                                  font=("Poppins", 20))
        self.label.pack(pady=10)
        
        #botão retornar
        self.back_button = ctk.CTkButton(self, 
                                         text="Voltar", 
                                         command=self.destroy)
        self.back_button.pack(pady=10)

class MenuAdicionarDispositivo (ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        
        #definição da janela
        self.title("Novo Dispositivo")
        self.geometry("400x240")
        
        #definição de etiquetas
        self.label = ctk.CTkLabel(self, 
                                  text="Novo Dispositivo", 
                                  font=("Poppins", 20))
        self.label.pack(pady=10)

        # Menu de opções
        self.opcoes = ["Lâmpada", "Ar Condicionado", "Televisão"]
        self.option_menu = ctk.CTkOptionMenu(self, 
                                             values=self.opcoes)
        self.option_menu.pack(pady=10)

        # Botão de confirmação
        self.confirm_button = ctk.CTkButton(self, 
                                            text="Confirmar", 
                                            command=self.confirmar_dispositivo)
        self.confirm_button.pack(pady=10)
        
        # Botão retornar
        self.back_button = ctk.CTkButton(self, 
                                         text="Voltar", 
                                         command=self.destroy)
        self.back_button.pack(pady=10)
        
        #botão retornar
        self.back_button = ctk.CTkButton(self, 
                                         text="Voltar", 
                                         command=self.destroy)
        self.back_button.pack(pady=10)

    def confirmar_dispositivo(self):
        escolha = self.option_menu.get()
        print(f"Dispositivo selecionado: {escolha}")
        self.destroy()

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
