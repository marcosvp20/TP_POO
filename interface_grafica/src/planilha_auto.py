from src.planilha import Planilha
import string

class PlanilhaAuto(Planilha):
    def __init__(self, nome_planilha) -> None:
        super().__init__(nome_planilha)
    
    #metodo para salvar várias automações com o mesmo nome
    def salvar(self, dados) -> None:
         for i in range(0, len(dados)):
            self.planilha[f'{string.ascii_uppercase[i]}{self.proxima_linha}'] = dados[i]
         self.workbook.save(self.nome_planilha)
         self.exclui_linha_vazia()
    
    #reotrona a linha de acordo com numero passado, contagem começa em 1
    def retorna_linha(self,numero_linha) -> list:
        linha = self.planilha[numero_linha]

        # Extrair os valores das células na linha
        valores_linha = [celula.value for celula in linha]

        return valores_linha
    