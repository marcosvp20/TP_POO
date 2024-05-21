import customtkinter as ctk

#definição do menu principal
class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        #definição da janela
        self.title("Menu Principal")
        self.geometry("800x480")
        
        #definição de etiquetas
        self.main_menu_label = ctk.CTkLabel(self, text="Menu Principal", font=("Poppins", 20))
        self.main_menu_label.pack(pady=25)
        
        #botão do menu de climatizadores
        self.button1 = ctk.CTkButton(self, text="Climatizadores", command=self.abrir_menu1)
        self.button1.pack(pady=25)
        
        #botão do menu de lâmpadas
        self.button2 = ctk.CTkButton(self, text="Lâmpadas", command=self.abrir_menu2)
        self.button2.pack(pady=25)

        #botão do menu de televisões
        self.button3 = ctk.CTkButton(self, text="Televisões", command=self.abrir_menu3)
        self.button3.pack(pady=25)
        
    def abrir_menu1(self) -> None:
        MenuClimatizador()
    
    def abrir_menu2(self) -> None:
        MenuLampada()

    def abrir_menu3(self) -> None:
        MenuTelevisao()


class MenuClimatizador(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        
        #definição da janela
        self.title("Menu de Climatizadores")
        self.geometry("400x240")
        
        #definição de etiquetas
        self.label = ctk.CTkLabel(self, text="Climatizadores", font=("Poppins", 20))
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
        self.title("Menu de Lâmpadas")
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
        self.title("Menu de Televisões")
        self.geometry("400x240")
        
        #definição de etiquetas
        self.label = ctk.CTkLabel(self, text="Televisões", font=("Poppins", 20))
        self.label.pack(pady=10)
        
        #botão retornar
        self.back_button = ctk.CTkButton(self, text="Voltar", command=self.destroy)
        self.back_button.pack(pady=10)


if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
