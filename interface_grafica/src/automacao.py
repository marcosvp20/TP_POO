from src.planilha import Planilha
from src.planilha_auto import PlanilhaAuto

class Automacao:
    #abre as planilhas e recebe o nome da automação
    def __init__(self, nome_auto:str) -> None:
        self.planilha_disp = Planilha('objetos.xlsx')
        self.planilha_auto = PlanilhaAuto('automacoes.xlsx')
        self.planilha_auto_temp = PlanilhaAuto('automacoestemp.xlsx')
        self.nome_auto = nome_auto
    
    def __salvar(self,dados:list,planilha:PlanilhaAuto) -> None:
        self.__planilha = planilha
        self.__planilha.salvar(dados)
        
    #adiciona as automações a planilha temporária
    def adicionar_auto_temp(self, dados:list) -> None:
        
        self.qnt_disp_auto = self.planilha_disp.retorna_quantidade_dispositivos()
        self.dados_auto = dados
        self.dados_auto.insert(0,self.nome_auto)
        self.dados_auto.insert(1,self.qnt_disp_auto)
        # self.planilha_auto_temp.salvar(self.dados_auto)
        self.__salvar(dados= dados, planilha=self.planilha_auto_temp)

    #exclui uma automação de acordo com o nome
    def excluir_auto(self,nome:str) -> bool:
        if self.planilha_auto.verifica_se_objeto_existe(nome):
            for i in range(0,self.__quantidade_automacoes(nome)):
                self.planilha_auto.excluir_dispositivo(nome)
            return True
        return False
    
    #exclui a planilha temporaria
    def __excluir_temp(self) -> None:
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
        self.planilha_auto.copia_planilha(planilha_origem = 'automacoestemp.xlsx')
        self.__excluir_temp()
        

# dados = ['Ar da sala', 23, True]
# dados2 =['Tv da sala', 52, True]
# dados3 = ['Ar da cozinha', 24, True]
# dados4 = ['Ar do quarto', 19, False]
# auto1 = Automacao('Bom dia')
# auto1.adicionar_auto_temp(dados)
# auto2 = Automacao('Boa tarde')
# auto2.adicionar_auto_temp(dados2)
# auto3 = Automacao('Hora de estudar')
# auto3.adicionar_auto_temp(dados3)
# auto4 = Automacao('Hora do almoço')
# auto4.adicionar_auto_temp(dados4)

# auto1.adicionar_auto()
# auto2.adicionar_auto()
# auto3.adicionar_auto()
# auto4.adicionar_auto()