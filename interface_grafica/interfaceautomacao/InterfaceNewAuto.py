import customtkinter as ctk
from src.frame import Frame
from interfacedispositivos.b_dinamico_disp import BotaoDinamicoDisp
from src.automacao import Automacao
from src.planilha_auto import PlanilhaAuto
from src.planilha import Planilha
from interfaceautomacao.InterfaceNameAuto import InterfaceNameAuto
from src.botao import Botao

class interfaceNewAuto:
    def __init__(self, janela) -> None:
        # self.__planilha_disp = Planilha('planilhas/objetos.xlsx')
        # self.__planilha_auto = PlanilhaAuto('planilhas/automacoestemp.xlsx')
        # self.__caminho_plan_disp = 'planilhas/objetos.xlsx'
        # self.__caminho_plan_autotemp = 'planilhas/automacoestemp.xlsx'
        self.auto = Automacao(None)
        

        """
        Inicializa a classe interfaceNewAuto.
        """
        self.janela = janela
        
    
    def cria_frame(self,mensagem:str) -> None:
        """
        Cria o frame para adicionar uma nova automação.
        """
        self.__frame = Frame(self.janela,mensagem)
        self.__frame_new_auto = self.__frame.retorna_frame()
        
    
    def insere_botoes(self) -> None:
        BotaoDinamicoDisp(self.janela, self.auto.planilha_auto_temp)
    
    def botaoProximo(self):
        nome_auto = InterfaceNameAuto(self.janela, self.auto)
        self.botao_proximo = Botao(janela=self.__frame_new_auto, posx=140, posy=560, texto='Próximo',
                                   comando=nome_auto.executar)
        self.botao_proximo.botao_menor('#f5e0df')

    def atualiza_temp(self) -> None:
        """
        Limpa a planilha temporária e a atualiza copiando da planilha de dispositivos atuais.
        """
        # auto = Automacao(None)
        # auto._excluir_temp()
        # auto.planilha_auto_temp.copia_planilha('planilhas/objetos.xlsx')
        self.auto._excluir_temp()
        self.auto.planilha_auto_temp.copia_planilha('planilhas/objetos.xlsx')
        self.auto.planilha_auto_temp.adiciona_coluna_de_selecao()

    def executar(self) -> None:
        """
        Executa a interface para adicionar uma nova automação.
        """
        if not self.auto.planilha_disp.verifica_se_esta_vazio():
            self.atualiza_temp()
            self.cria_frame('Adicionar automação: ')
            self.insere_botoes()
            self.botaoProximo()
        else:
            self.cria_frame('Adicione dispositivos\npara criar automações')
        
        