from planilha import  Planilha
from planilha_auto import PlanilhaAuto

class Automacao:
    #abre as planilhas e recebe o nome da automação
    def __init__(self, nome_auto:str) -> None:
        self.planilha_disp = Planilha('objetos.xlsx')
        self.planilha_auto = PlanilhaAuto('automacoes.xlsx')
        self.planilha_auto_temp = PlanilhaAuto('automacoestemp.xlsx')
        self.nome_auto = nome_auto
    
    #adiciona as automações a planilha temporária
    def adicionar_auto_temp(self, dados:list) -> None:
        
        self.qnt_disp_auto = self.planilha_disp.retorna_quantidade_dispositivos()
        self.dados_auto = dados
        self.dados_auto.insert(0,self.nome_auto)
        self.dados_auto.insert(1,self.qnt_disp_auto)
        self.planilha_auto_temp.salvar(self.dados_auto)

    #exclui uma automação de acordo com o nome
    def excluir_auto(self,nome:str) -> bool:
        if self.planilha_auto.verifica_se_objeto_existe(nome):
            for i in range(0,self.__quantidade_automacoes(nome)):
                self.planilha_auto.excluir_dispositivo(nome)
            return True
        return False
    
    #exclui a planilha temporaria
    def __excluir_temp(self) -> bool:
        self.planilha_auto_temp.limpar_planilha()
    
    #retorna a quantidade de automações com o nome informado
    def __quantidade_automacoes(self, nome:str) -> int:
        self.__quantidade = 0
        nomes_auto = self.planilha_auto.retorna_nome()
        for i in range(0, len(nomes_auto)):
            if nomes_auto[i] == nome:
                self.__quantidade += 1
        return self.__quantidade
    
    #adiciona as automações da planilha temporária para a planilha principal
    def adicionar_auto(self) -> None:
        self.__qnt_col = self.planilha_auto_temp.retorna_coluna(1)
        print(len(self.__qnt_col))
        
        for i in range(0,len(self.__qnt_col)):
            print(i)
            dados = self.planilha_auto_temp.retorna_linha(i+1)
            self.planilha_auto.salvar(dados)
        self.__excluir_temp()
        
for i in range (0,5):                 
    auto = Automacao('boa tarde')
    auto.adicionar_auto_temp(['ar da sala', 23, True])

auto.adicionar_auto()