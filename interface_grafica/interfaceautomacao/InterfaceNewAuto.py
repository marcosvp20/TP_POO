import customtkinter as ctk
from src.frame import Frame
from interfacedispositivos.b_dinamico_disp import BotaoDinamicoDisp
from src.automacao import Automacao
from src.planilha_auto import PlanilhaAuto
from src.planilha import Planilha

class interfaceNewAuto:
    def __init__(self, janela) -> None:
        self.__planilha_disp = Planilha('planilhas/objetos.xlsx')
        self.__planilha_auto = PlanilhaAuto('planilhas/automacoestemp.xlsx')
        self.__caminho_plan_disp = 'planilhas/objetos.xlsx'
        self.__caminho_plan_autotemp = 'planilhas/automacoestemp.xlsx'
        """
        Inicializa a classe interfaceNewAuto.
        """
        self.janela = janela
        pass
    
    def cria_frame(self) -> None:
        """
        Cria o frame para adicionar uma nova automação.
        """
        self.frame_new_auto = Frame(self.janela, 'Adicionar automação: ', '').frame
        
    
    def insere_botoes(self) -> None:
        auto = Automacao('')
        self.__planilha_auto.copia_planilha(self.__caminho_plan_disp)
        BotaoDinamicoDisp(self.janela, self.__caminho_plan_autotemp)
        auto._excluir_temp()
    
    def botaoProximo(self):

        self.botao_proximo = ctk.CTkButton(master=self.frame_new_auto, 
                                           width=170, 
                                           height=50, 
                                           font=('League Spartan bold',17), 
                                           fg_color='#f5e0df', 
                                           corner_radius=0, 
                                           text='Próximo', 
                                           text_color='black', 
                                           command=None)
        self.botao_proximo.place(x=140, y=560)
        
    def executar(self) -> None:
        """
        Executa a interface para adicionar uma nova automação.
        """
        self.cria_frame()
        # auto = Automacao('')
        # auto._Automacao__excluir_temp()
        # auto.planilha_auto_temp = auto.planilha_disp
        # BotaoDinamicoDisp(self.janela, 'planilhas/automacoestemp.xlsx')
        self.insere_botoes()
        self.botaoProximo()
        
        