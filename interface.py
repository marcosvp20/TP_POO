import customtkinter as ctk
from PIL import Image, ImageTk
import os
from arcondicionado import ArCondicionado
from caixa_de_som import Caixa_de_som
from fechadura import Fechadura
from lampada import Lampada
from televisao import Televisao

#definição do menu principal
class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        #definição da janela
        self.title("Menu Principal")
        self.geometry("800x600")
        
        #definição de etiquetas
        self.main_menu_label = ctk.CTkLabel(self, text="Menu Principal", font=("Arial Bold", 20))
        self.main_menu_label.pack(pady=50)
        
        #botão do menu dos Ar Condicionado
        img1 = ctk.CTkImage(light_image=Image.open("imagens/arcondicionado.png"), 
                           dark_image=Image.open("imagens/arcondicionado.png"),
                           size = (30,30))
        self.button1 = ctk.CTkButton(self, 
                                     text="Ar Condicionado", 
                                     command=self.abrir_menu1, 
                                     width = 150,
                                     height=50,
                                     fg_color="blue",
                                     hover_color= "#4e31ff",
                                     text_color="white",
                                     font = ("arial bold", 18),
                                     corner_radius=20,
                                     state = "normal",
                                     image=img1).pack(pady=25)
        
        #botão do menu de lâmpadas
        img2 = ctk.CTkImage(light_image=Image.open("imagens/led-inteligente.png"), 
                           dark_image=Image.open("imagens/led-inteligente.png"),
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
                           size = (30,30))
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
        self.label = ctk.CTkLabel(self, text="Ar condicionados", font=("Poppins", 20))
        self.label.pack(pady=10)

        #criação de um slider
        self.slider_label = ctk.CTkLabel(self, text="Temperatura")
        self.slider_label.pack(pady=10)

        self.slider = ctk.CTkSlider(self, from_=15, to=30, command=self.definir_temperatura)
        self.slider.pack(pady=10)

        self.slider_value_label = ctk.CTkLabel(self, text="15")
        self.slider_value_label.pack(pady=10)
        
        #botão retornar
        self.back_button = ctk.CTkButton(self, text="Voltar", command=self.destroy)
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
        self.label = ctk.CTkLabel(self, text="Lâmpadas", font=("Poppins", 20))
        self.label.pack(pady=10)
        
        #botão retornar
        self.back_button = ctk.CTkButton(self, text="Voltar", command=self.destroy)
        self.back_button.pack(pady=10)

class MenuTelevisao(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        
        #definição da janela
        self.title("Menu dos Televisões")
        self.geometry("400x240")
        
        #definição de etiquetas
        self.label = ctk.CTkLabel(self, text="Televisões", font=("Poppins", 20))
        self.label.pack(pady=10)
        
        #botão retornar
        self.back_button = ctk.CTkButton(self, text="Voltar", command=self.destroy)
        self.back_button.pack(pady=10)

class MenuAdicionarDispositivo (ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        
        #definição da janela
        self.title("Novo Dispositivo")
        self.geometry("800x600")
        
        #definição de etiquetas
        self.label = ctk.CTkLabel(self, text="Novo Dispositivo", font=("Poppins", 20))
        self.label.pack(pady=10)

        # Menu de opções
        self.opcoes = ["Ar Condicionado", "Caixa de Som", "Fechadura", "Lâmpada", "Televisão"]
        self.option_menu = ctk.CTkOptionMenu(self, values=self.opcoes)
        self.option_menu.pack(pady=10)

        # Botão de confirmação
        self.confirm_button = ctk.CTkButton(self, text="Confirmar", command=self.confirmar_dispositivo)
        self.confirm_button.pack(pady=10)
        
        # Botão retornar
        self.back_button = ctk.CTkButton(self, text="Voltar", command=self.destroy)
        self.back_button.pack(pady=10)

        self.entry = None
        self.submit_button = None
        self.novo_nome = None

    # Confirmação da classe do novo dispositivo
    def confirmar_dispositivo(self):
        escolha = self.option_menu.get()
        print(f"Dispositivo selecionado: {escolha}")
        self.solicitar_nome(escolha)

    # Solicita o nome do novo dispositivo ao usuário
    def solicitar_nome(self, escolha):
        # Criar campo de entrada
        self.entry = ctk.CTkEntry(self, placeholder_text="Defina o nome do novo dispositivo: ")
        self.entry.pack(pady=20)
        
        # Botão para usar o texto do campo de entrada
        self.submit_button = ctk.CTkButton(self, text="Confirmar", command=lambda: self.use_text(escolha))
        self.submit_button.pack(pady=20)

    # Função para acessar o texto da entry e criar o novo objeto
    def use_text(self, escolha):
        if self.entry: #garantir que não está vazio
            self.novo_nome = self.entry.get()
            if self.novo_nome:
                match(escolha):
                    case "Ar Condicionado":
                        ArCondicionado(self.novo_nome)
                        print(f"Novo A/C adicionado: {self.novo_nome}")
                    case "Caixa de Som":
                        Caixa_de_som(self.novo_nome)
                        print(f"Nova Caixa de Som adicionada: {self.novo_nome}")
                    case "Fechadura":
                        Fechadura(self.novo_nome)
                        print(f"Nova Fechadura adicionada: {self.novo_nome}")
                    case "Lâmpada":
                        Lampada(self.novo_nome)
                        print(f"Nova Lâmpada adicionada: {self.novo_nome}")
                    case "Televisão":
                        Televisao(self.novo_nome)
                        print(f"Nova TV adicionada: {self.novo_nome}")

                self.entry.destroy()
                self.submit_button.destroy()

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
