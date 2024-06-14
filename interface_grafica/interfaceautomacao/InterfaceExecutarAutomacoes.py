from PIL import Image
import customtkinter as ctk
from src.automacao import Automacao
from src.frame import Frame
from src.botao import Botao

class interfaceAutomacao:
    def __init__(self, janela:ctk, nome:str) -> None:
        self.janela = janela
        self.nome = nome

    def criarframe(self) -> None:
        """
        Cria o frame para exibir ações da automação.
        """
        self.__frame = Frame(self.janela, self.nome, '')
        self.__frame_automacoes = self.__frame.retorna_frame()
    
    def botaoAtivar(self) -> None:
        self.botao_ativar = Botao(janela=self.__frame_automacoes, posx=140, posy=260,
                                  texto='Ativar', comando=self.__click_ativar)
        self.botao_ativar.botao_menor('#f5e0df')
    
    def __click_ativar(self) -> None:
        auto = Automacao(self.nome)
        auto.executar_automacao()
        self.__frame.mensagem('Automação ativada com sucesso!')
        self.__frame.destroy()
        from interfaceautomacao.interfaceAutomações import interfaceAutomacoes
        auto = interfaceAutomacoes(self.janela)
        auto.executar()
        

    def botaoExcluir(self) -> None:
        """
        Cria o botão de exclusão da automação.
        """
        image = ctk.CTkImage(light_image=Image.open('imagens/excluir.png'), size=(20,20))
        self.botao_excluir = Botao(janela=self.__frame_automacoes, posx=140, posy=500,
                                  texto='Excluir automação', comando=self.__click_excluir, imagem=image)
        self.botao_excluir.botao_menor('#f5e0df')

    def __click_excluir(self) -> None:
        auto = Automacao(self.nome)
        if auto.excluir_auto():
            self.__frame.mensagem('A automação foi excluída com sucesso!')
            self.__frame.destroy()
            from interfaceautomacao.interfaceAutomações import interfaceAutomacoes
            auto = interfaceAutomacoes(self.janela)
            auto.executar()
        else:
            self.frame.mensagem('Falha ao excluir a automação')
        
    def executar(self) -> None:
        self.criarframe()
        self.botaoAtivar()
        self.botaoExcluir()