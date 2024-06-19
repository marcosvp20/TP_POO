from interface_grafica.menuautomacao.interfaces_auto.IMenuNewAuto import IMenuNewAuto
import customtkinter as ctk
from interface_grafica.src.frame import Frame
from interface_grafica.menudispositivos.b_dinamico_disp import BotaoDinamicoDisp
from interface_grafica.src.automacao import Automacao
from interface_grafica.menuautomacao.MenuNameAuto import MenuNameAuto
from interface_grafica.src.botao import Botao

class MenuNewAuto(IMenuNewAuto):
    """
    Classe que representa o menu da definição de uma nova automação.
    """
    def __init__(self, janela:ctk.CTk) -> None:
        """
        Inicializa o menu de definição de uma nova automação.

        Argumentos:
            janela(ctk.ctk): Janela onde o frame da interface será fixado.
        """
        self.auto = Automacao(None)
        self.janela = janela
        
    
    def cria_frame(self, mensagem1:str, mensagem2:str) -> None:
        """
        Cria o frame para adicionar uma nova automação.

        Args:
            mensagem1(str): Texto a ser exibido na primeira linha do frame.
            mensagem2(str): Texto a ser exibido na segunda linha do frame.
        """
        self.__frame = Frame(self.janela, mensagem1, mensagem2)
        self.__frame_new_auto = self.__frame.retorna_frame()
        
    
    def insere_botoes(self) -> None:
        """
        Instancia um botão dinâmico de dispostivos para exibir na tela os dispositivos disponíveis.
        """
        BotaoDinamicoDisp(self.janela, self.auto.planilha_auto_temp)
    
    def botaoProximo(self):
        """
        Adiciona um botão que avança para o menu de definição do nome da automação.
        """
        nome_auto = MenuNameAuto(self.janela, self.auto)
        self.botao_proximo = Botao(janela=self.__frame_new_auto, posx=140, posy=560, texto='Próximo',
                                   comando=nome_auto.executar)
        self.botao_proximo.botao_menor('white')

    def atualiza_temp(self) -> None:
        """
        Limpa a planilha temporária e a atualiza copiando da planilha de dispositivos atuais.
        """
        self.auto._excluir_temp()
        self.auto.planilha_auto_temp.copia_planilha('planilhas/objetos.xlsx')
        self.auto.planilha_auto_temp.adiciona_coluna_de_selecao()

    def executar(self) -> None:
        """
        Executa a interface para adicionar uma nova automação.
        """
        if not self.auto.planilha_disp.verifica_se_esta_vazio():
            self.atualiza_temp()
            self.cria_frame('Adicionar automação: ', '')
            self.insere_botoes()
            self.botaoProximo()
        else:
            self.cria_frame('Adicione dispositivos', 'para criar automações')
        
        