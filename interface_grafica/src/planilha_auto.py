from src.planilha import Planilha
import string
import openpyxl

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
    
    def copia_planilha(self, planilha_origem) -> None:
        workbook_src = openpyxl.load_workbook(planilha_origem)
        sheet_src = workbook_src.active
        if sheet_src.max_row == 1 and sheet_src.max_column == 1 and sheet_src.cell(1, 1).value is None:
            return
        else:
            for row in sheet_src.iter_rows(values_only=True):
                self.planilha.append(row)
            
            self.workbook.save(self.nome_planilha)