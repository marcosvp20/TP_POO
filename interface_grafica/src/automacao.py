from src.planilha import Planilha
from src.planilha_auto import PlanilhaAuto

class Automacao:
    def __init__(self, nome_auto:str) -> None:
        """
        Inicializa a classe Automacao.

        Args:
            nome_auto (str): O nome da automação.
        """
        self.planilha_disp = Planilha('planilhas/objetos.xlsx')
        self.planilha_auto = PlanilhaAuto('planilhas/automacoes.xlsx')
        self.planilha_auto_temp = PlanilhaAuto('planilhas/automacoestemp.xlsx')
        self.nome_auto = nome_auto
        self.qnt_linhas_auto = len(self.planilha_auto.retorna_linha(1))
    def excluir_auto(self,nome:str,coluna = None) -> bool:
        """
        Exclui uma automação de acordo com o nome.

        Args:
            nome (str): O nome da automação a ser excluída.

        Returns:
            bool: True se a automação foi excluída com sucesso, False caso contrário.
        """
        if coluna == None:
            if self.planilha_auto.verifica_se_objeto_existe(nome):
                for i in range(0,self.__quantidade_automacoes(nome)):
                    self.planilha_auto.excluir_dispositivo(nome)
                return True
            return False
        else:
            for i in range(0,len(self.planilha_auto.retorna_coluna(1))):
                print('2')
                self.planilha_auto.excluir_linha(nome, coluna)

    def _excluir_temp(self) -> None:
        """
        Exclui a planilha temporária.
        """
        self.planilha_auto_temp.limpar_planilha()
    
    def __quantidade_automacoes(self, nome:str) -> int:
        """
        Retorna a quantidade de automações com o nome informado.

        Args:
            nome (str): O nome da automação.

        Returns:
            int: A quantidade de automações com o nome informado.
        """
        self.__quantidade = 0
        nomes_auto = self.planilha_auto.retorna_nome()
        for i in range(0, len(nomes_auto)):
            if nomes_auto[i] == nome:
                self.__quantidade += 1
        return self.__quantidade
    
    def adicionar_auto(self) -> bool:
        """
        Adiciona as automações da planilha temporária para a planilha principal.
        """
        self.qnt_linhas_auto = self.planilha_disp.retorna_quantidade_dispositivos() #retorna a quantidade de linhas da planilha
        
        if not self.planilha_auto.verifica_se_objeto_existe(self.nome_auto):
            # for i in range(1,self.qnt_linhas_auto+1):
            #     self.dados_auto = self.planilha_auto_temp.retorna_linha(i)
            #     self.dados_auto.insert(0,self.nome_auto)
            #     print(self.dados_auto)
            #     self.planilha_auto.salvar(self.dados_auto)
            # self._excluir_temp()
            
            self.planilha_auto_temp.adicionar_nome_primeira_celula(self.nome_auto)
            self.planilha_auto.copia_planilha('planilhas/automacoestemp.xlsx')
            self._excluir_temp()
            
            return True
        else:
            return False

            
    def retorna_nomes_auto(self) -> list:
        """
        Retorna uma lista com os nomes das automações sem repetição
        """
        self.__nomes_auto_temp = self.planilha_auto.retorna_coluna(1)
        self.__nomes_auto = list(set(self.__nomes_auto_temp))
        
        return self.__nomes_auto

    def executar_automacao(self, nome_auto:str) -> None:
        """
        executa a automação informada, alterando os parâmetros do objeto na planilha dispositivos
        
        args:
        nome_auto (str): nome da automação a ser executada"""
        
        for i in range(0, self.qnt_linhas_auto):
            linha = self.planilha_auto.retorna_linha(i+1)
            if linha[i] == nome_auto:
                linha.pop(0)
                for j in range(1,len(linha)):
                    self.planilha_disp.editar(linha, j)
            
            
        
a = Automacao(None)
a.excluir_auto('t')
