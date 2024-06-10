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
    
    def __salvar(self,dados:list,planilha:PlanilhaAuto) -> None:
        """
        Salva os dados na planilha especificada.

        Args:
            dados (list): Os dados a serem salvos.
            planilha (PlanilhaAuto): A planilha onde os dados serão salvos.
        """
        self.__planilha = planilha
        self.__planilha.salvar(dados)
        
    def adicionar_auto_temp(self) -> None:
        """
        Adiciona as automações à planilha temporária.

        Args:
            dados (list): Os dados das automações a serem adicionadas.
        """
        pass

    def excluir_auto(self,nome:str) -> bool:
        """
        Exclui uma automação de acordo com o nome.

        Args:
            nome (str): O nome da automação a ser excluída.

        Returns:
            bool: True se a automação foi excluída com sucesso, False caso contrário.
        """
        if self.planilha_auto.verifica_se_objeto_existe(nome):
            for i in range(0,self.__quantidade_automacoes(nome)):
                self.planilha_auto.excluir_dispositivo(nome)
            return True
        return False
    
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
    
    def adicionar_auto(self) -> None:
        """
        Adiciona as automações da planilha temporária para a planilha principal.
        """
        self.qnt_disp_auto = self.planilha_disp.retorna_quantidade_dispositivos()
        for i in range(1,self.qnt_disp_auto+1):
            self.dados_auto = self.planilha_auto_temp.retorna_linha(i)
            self.dados_auto.insert(0,self.nome_auto)
            print(self.dados_auto)
            self.planilha_auto.salvar(self.dados_auto)
            #self.dados_auto.insert(1,self.qnt_disp_auto)
            #self.__salvar(dados= self.dados_auto, planilha=self.planilha_auto)
        self._excluir_temp()

            
    def retorna_nomes_auto(self) -> list:
        """
        Retorna uma lista com os nomes das automações sem repetição
        """
        self.__nomes_auto_temp = self.planilha_auto.retorna_coluna(1)
        self.__nomes_auto = list(set(self.__nomes_auto_temp))
        
        return self.__nomes_auto
