import customtkinter as ctk
from src.frame import Frame
from interfacedispositivos.b_dinamico_disp import BotaoDinamicoDisp
from src.automacao import Automacao
from src.planilha_auto import PlanilhaAuto
from src.planilha import Planilha
from interfaceautomacao.InterfaceNameAuto import InterfaceNameAuto

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
    
    def cria_frame(self,mensagem:str) -> None:
        """
        Cria o frame para adicionar uma nova automação.
        """
        self.frame_new_auto = Frame(self.janela,mensagem).frame
        
    
    def insere_botoes(self) -> None:
        auto = Automacao('')
        self.__planilha_auto.copia_planilha(self.__caminho_plan_disp)
        BotaoDinamicoDisp(self.janela, self.__caminho_plan_autotemp)
        auto._excluir_temp()
    
    def botaoProximo(self):
        nome_auto = InterfaceNameAuto(self.janela)
        self.botao_proximo = ctk.CTkButton(master=self.frame_new_auto, 
                                           width=170, 
                                           height=50, 
                                           font=('League Spartan bold',17), 
                                           fg_color='#f5e0df', 
                                           corner_radius=0, 
                                           text='Próximo', 
                                           text_color='black', 
                                           command=nome_auto.executar)
        self.botao_proximo.place(x=140, y=560)
        
    def executar(self) -> None:
        """
        Executa a interface para adicionar uma nova automação.
        """
        if not self.__planilha_disp.verifica_se_esta_vazio():
            self.cria_frame('Adicionar automação: ')
            # auto = Automacao('')
            # auto._Automacao__excluir_temp()
            # auto.planilha_auto_temp = auto.planilha_disp
            # BotaoDinamicoDisp(self.janela, 'planilhas/automacoestemp.xlsx')
            self.insere_botoes()
            self.botaoProximo()
        else:
            self.cria_frame('Adicione dispositivos\npara criar automações')
        
        