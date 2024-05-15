import openpyxl
import string

#Classe para facilitar na hora de salvar o status dos itens da casa

class Planilha:
   
   #abre a planilha
   def __init__(self,nome_planilha) -> None:
      self.nome_planilha = nome_planilha
      self.workbook = openpyxl.load_workbook(self.nome_planilha)
      self.planilha = self.workbook['Sheet1']
      self.proxima_linha = self.planilha.max_row
      
   #salva um lista de dados na planilha
   #PRÉ CONDIÇÃO: O nome precisa ser o primeiro na lista de dados
   def salvar(self, dados):
      if not self.verifica_se_objeto_existe(dados[0]):
         for i in range(0, len(dados)):
            print(string.ascii_uppercase[i], self.proxima_linha)
            self.planilha[f'{string.ascii_uppercase[i]}{self.proxima_linha}'] = dados[i]
         self.workbook.save(self.nome_planilha)
   
   #edita o status do objeto
   #não edita o nome
   def editar(self, nome, num_col, novo_dado):
      i = 1
      for linha in self.planilha.iter_rows(min_row=1, values_only=True) :
         if linha[0] == nome:
            celula = self.planilha[f'{string.ascii_uppercase[num_col-1]}{i}']
            celula.value = novo_dado
            self.workbook.save(self.nome_planilha)
      i += 1
   #verifica se o objeto já está cadastrado
   def verifica_se_objeto_existe(self,nome):
      for linha in self.planilha.iter_rows(min_row=1, values_only=True) :
         if linha[0] == nome:
            return True
         return False
   #Retorna o valor da coluna desejada a partir do nome do objeto
   def retorna_valor(self, nome, coluna):
      for linha in self.planilha.iter_rows(min_row=1, values_only=True) :
         if linha[0] == nome:
            return linha[coluna-1]