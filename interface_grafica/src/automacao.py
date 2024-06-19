from interface_grafica.src.interfaces_src.IAutomação import IAutomacao
from interface_grafica.src.planilha import Planilha
from interface_grafica.src.planilha_auto import PlanilhaAuto

class Automacao(IAutomacao):
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
        self.qnt_linhas_auto = self.planilha_auto.retorna_quantidade_linhas()
        
    def excluir_auto(self,coluna = None) -> bool:
        """
        Exclui uma automação de acordo com o nome.

        Args:
            nome (str): O nome da automação a ser excluída.

        Returns:
            bool: True se a automação foi excluída com sucesso, False caso contrário.
        """
        if coluna == None:
            if self.planilha_auto.verifica_se_objeto_existe(self.nome_auto):
                if not self.planilha_auto.verifica_se_esta_vazio():
                    for i in range(0,self.__quantidade_automacoes(self.nome_auto)):
                        self.planilha_auto.excluir_dispositivo(self.nome_auto)
                return True
            return False
        else:
            if not self.planilha_auto.verifica_se_esta_vazio():
                for i in range(0,len(self.planilha_auto.retorna_coluna('A'))):
                    self.planilha_auto.excluir_linha(self.nome_auto, coluna)

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
        nomes_auto = self.planilha_auto.retorna_coluna('A')
        for i in range(0, len(nomes_auto)):
            if nomes_auto[i] == nome:
                self.__quantidade += 1
        return self.__quantidade
    
    def adicionar_auto(self) -> bool:
        """
        Adiciona as automações da planilha temporária para a planilha principal.

        Returns:
            bool: True se a automação foi adicionada com sucesso, False caso contrário.
        """
        self.qnt_linhas_auto = self.planilha_disp.retorna_quantidade_linhas() #retorna a quantidade de linhas da planilha
        
        if not self.planilha_auto.verifica_se_objeto_existe(self.nome_auto):
            self.verifica_alteracoes()
            self.planilha_auto_temp.excluir_coluna_de_selecao()
            self.planilha_auto_temp.adicionar_nome_primeira_celula(self.nome_auto)
            self.planilha_auto.copia_planilha('planilhas/automacoestemp.xlsx')
            self._excluir_temp() # Garantir que a planilha temporária é limpada.
            
            return True
        else:
            return False

            
    def retorna_nomes_auto(self) -> list:
        """
        Retorna uma lista com os nomes das automações sem repetição
        """
        self.__nomes_auto_temp = self.planilha_auto.retorna_coluna('A')
        self.__nomes_auto = list(set(self.__nomes_auto_temp))
        
        return self.__nomes_auto

    def executar_automacao(self) -> None:
        """
        Executa a automação informada, alterando os parâmetros do objeto na planilha dispositivos
        
        Argumentos:
            nome_auto (str): Nome da automação a ser executada
        """
        
        for i in range(0, self.qnt_linhas_auto):
            linha = self.planilha_auto.retorna_linha(i+1)
            if linha[0] == self.nome_auto:
                linha.pop(0)
                for j in range(1,len(linha)):
                    self.planilha_disp.editar(linha, j)
    
    def verifica_alteracoes(self) -> None:
        """
        Verifica quais linhas da planilha de automações temporárias não foram selecionadas e as excluem.
        """
        linha_a_excluir = []
        for i in range(1, len(self.planilha_auto_temp.retorna_coluna('A'))+1):
            linha_auto_temp = self.planilha_auto_temp.retorna_linha(i)

            # Verifica se a 6ª coluna está definida como False
            if linha_auto_temp[5] == False:
                linha_a_excluir.append(linha_auto_temp[0])

        for id_linha in linha_a_excluir:
            self.planilha_auto_temp.excluir_linha(id_linha, 0)
