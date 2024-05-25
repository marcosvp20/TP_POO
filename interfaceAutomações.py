import customtkinter as ctk

class interfaceAutomacoes:
    def __init__(self, janela) -> None:
        self.janela = janela
        
        
    def criaframe(self) -> None:
         self.frame_automacoes = ctk.CTkFrame(self.janela, width=800, height=500, fg_color='black', corner_radius=0)
        
    def textosuperior(self) -> None:
        self.texto_superior = ctk.CTkLabel(self.frame_automacoes, width=200, height=50, text='Automações',
                                           font=('Rockweel', 25), text_color='#cbcbcb')
        self.texto_superior.place(x = 0, y = 15)
    
    def botao1(self) -> None:
        self.botao_1 = ctk.CTkButton(master=self.frame_automacoes, text='Bom dia',
                                    font=('Rockwell', 15), width=300, height=55, fg_color='#2a2a2a',
                                    corner_radius=35)
        self.botao_1.place(x = 25, y = 125)
    
    def botao2(self) -> None:
        self.botao_2 = ctk.CTkButton(master=self.frame_automacoes, text='Chengando em\ncasa',
                                    font=('Rockwell', 15), width=300, height=55, fg_color='#2a2a2a',
                                    corner_radius=35)
        self.botao_2.place(x = 25, y = 215)
    
    def botao3(self) -> None:
        self.botao_3 = ctk.CTkButton(master=self.frame_automacoes, text='Hora da\nlimpeza',
                                    font=('Rockwell', 15), width=300, height=55, fg_color='#2a2a2a',
                                    corner_radius=35)
        self.botao_3.place(x = 25, y = 305)
    
    def botao4(self) -> None:
        self.botao_4 = ctk.CTkButton(master=self.frame_automacoes, text='Hora da\nlimpeza',
                                    font=('Rockwell', 15), width=300, height=55, fg_color='#2a2a2a',
                                    corner_radius=35)
        self.botao_4.place(x = 475, y = 125)
    
    def botao5(self) -> None:
        self.botao_5 = ctk.CTkButton(master=self.frame_automacoes, text='Hora de\nestudar',
                                    font=('Rockwell', 15), width=300, height=55, fg_color='#2a2a2a',
                                    corner_radius=35)
        self.botao_5.place(x = 475, y = 215)
        
    def botao6(self) -> None:
        self.botao_6 = ctk.CTkButton(master=self.frame_automacoes, text='Hora de\ndormir',
                                    font=('Rockwell', 15), width=300, height=55, fg_color='#2a2a2a',
                                    corner_radius=35)
        self.botao_6.place(x = 475, y = 305)
    
    def botaop1(self) -> None:
        self.botao_personalizado_1 = ctk.CTkButton(master=self.frame_automacoes, text='Automação personalizada 1',
                                    font=('Rockwell', 15), width=300, height=55, fg_color='#2a2a2a',
                                    corner_radius=35)
        self.botao_personalizado_1.place(x = 25, y = 395)
    
    def botaop2(self) -> None:
        self.botao_personoalizado_2 = ctk.CTkButton(master=self.frame_automacoes, text='Automação personalizada 2',
                                    font=('Rockwell', 15), width=300, height=55, fg_color='#2a2a2a',
                                    corner_radius=35)
        self.botao_personoalizado_2.place(x = 475, y = 395)
        
    def executar(self) -> None:
        self.criaframe()
        self.textosuperior()
        self.botao1()
        self.botao2()
        self.botao3()
        self.botao4()
        self.botao5()
        self.botao6()
        self.botaop1()
        self.botaop2()
        self.frame_automacoes.place(x = 0, y = 0)