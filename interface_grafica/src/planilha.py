import openpyxl
import string

class Planilha:
   """
   Classe para facilitar na hora de salvar o status dos itens da casa.
   """

   def __init__(self, nome_planilha):
      """
      Inicializa a classe Planilha.

      Args:
         nome_planilha (str): O nome do arquivo da planilha.
      """
      self.nome_planilha = nome_planilha
      self.workbook = openpyxl.load_workbook(self.nome_planilha)
      self.planilha = self.workbook['Sheet1']
      self.proxima_linha = self.planilha.max_row + 1
      if not self.verifica_se_esta_vazio():
         self.exclui_linha_vazia()

   def salvar(self, dados):
      """
      Salva uma lista de dados na planilha.

      Args:
         dados (list): A lista de dados a serem salvos.

      Returns:
         bool: True se os dados foram salvos com sucesso, False caso contrário.
      """
      if not self.verifica_se_objeto_existe(dados[0]):
         for i in range(0, len(dados)):
            self.planilha[f'{string.ascii_uppercase[i]}{self.proxima_linha}'] = dados[i]
         self.workbook.save(self.nome_planilha)
         self.exclui_linha_vazia()
         return True
      return False

   def editar(self, dados:list, coluna:int):
      """
      Edita o status do objeto na planilha.

      Args:
         dados (list): A lista de dados contendo o nome e o novo status do objeto.
         coluna (int): O número da coluna onde o status será atualizado.
      """
      i = 1
      for linha in self.planilha.iter_rows(min_row=1, values_only=True):
         if linha[0] == dados[0]:
            cell = self.planilha[f'{string.ascii_uppercase[coluna]}{i}']
            cell.value = dados[coluna]
            self.workbook.save(self.nome_planilha)
         i += 1

   def verifica_se_objeto_existe(self, nome: str):
      """
      Verifica se o objeto já está cadastrado na planilha.

      Args:
         nome (str): O nome do objeto a ser verificado.

      Returns:
         bool: True se o objeto já existe na planilha, False caso contrário.
      """
      if not self.verifica_se_esta_vazio():
         for linha in self.planilha.iter_rows(min_row=1, values_only=True):
            if linha[0].upper() == nome.upper():
               return True
      return False

   def retorna_valor(self, nome, coluna):
      """
      Retorna o valor da coluna desejada a partir do nome do objeto.

      Args:
         nome (str): O nome do objeto.
         coluna (int): O número da coluna desejada.

      Returns:
         str: O valor da coluna do objeto.
      """
      for linha in self.planilha.iter_rows(min_row=1, values_only=True):
         if linha[0] == nome:
            return linha[coluna-1]

   def exclui_linha_vazia(self):
      """
      Exclui as linhas vazias da planilha.
      """
      i = 1
      for linha in self.planilha.iter_rows(min_row=1, values_only=True):
         linhas_vazias = 0
         for j in range(0, len(linha)):
            if linha[j] == None:
               linhas_vazias += 1
         if linhas_vazias == len(linha):
            self.planilha.delete_rows(i)
            self.workbook.save(self.nome_planilha)
         i += 1

   def retorna_quantidade(self, tipo:str):
      """
      Retorna a quantidade da classe de objetos presente na planilha.

      Args:
         tipo (str): O tipo de objeto.

      Returns:
         int: A quantidade de objetos do tipo especificado.
      """
      quantidade = 0
      if not self.verifica_se_esta_vazio():
         for linha in self.planilha.iter_rows(min_row=1, values_only=True):
            if linha[1] == tipo:
               quantidade += 1
         return quantidade
      else:
         return 0

   def verifica_se_esta_vazio(self):
      """
      Verifica se a planilha está vazia.

      Returns:
         bool: True se a planilha está vazia, False caso contrário.
      """
      for row in self.planilha.iter_rows():
         for cell in row:
            if cell.value is not None:
               return False
      return True

   def retorna_quantidade_dispositivos(self):
      """
      Retorna a quantidade de dispositivos presentes na planilha.

      Returns:
         int: A quantidade de dispositivos presentes na planilha.
      """
      if self.verifica_se_esta_vazio():
         return 0
      return self.planilha.max_row

   def retorna_nome(self):
      """
      Retorna uma lista com os nomes dos objetos presentes na planilha.

      Returns:
         list: Uma lista com os nomes dos objetos.
      """
      if not self.verifica_se_esta_vazio():
         nomes = []
         for linha in self.planilha.iter_rows(min_row=1, values_only=True):
            nomes.append(linha[0])
         return nomes
      else:
         return None

   def retorna_tipos(self):
      """
      Retorna uma lista com os tipos dos objetos presentes na planilha.

      Returns:
         list: Uma lista com os tipos dos objetos.
      """
      if not self.verifica_se_esta_vazio():
         tipos = []
         for linha in self.planilha.iter_rows(min_row=1, values_only=True):
            tipos.append(linha[1])
         return tipos
      else:
         return None

   def excluir_dispositivo(self, nome):
      """
      Exclui um dispositivo da planilha.

      Args:
         nome (str): O nome do dispositivo a ser excluído.

      Returns:
         bool: True se o dispositivo foi excluído com sucesso, False caso contrário.
      """
      linha_a_excluir = 1
      for linha in self.planilha.iter_rows(min_row=1, values_only=True):
         if linha[0] == nome:
            self.planilha.delete_rows(linha_a_excluir)
            self.workbook.save(self.nome_planilha)
            return True
         linha_a_excluir += 1
      return False

   def retorna_coluna(self, coluna:int):
      """
      Retorna uma lista com os valores da coluna especificada.

      Args:
         coluna (int): O número da coluna.

      Returns:
         list: Uma lista com os valores da coluna.
      """
      dados = []
      for linha in self.planilha.iter_rows(min_row=1, max_row=self.retorna_quantidade_dispositivos(), values_only=True):
         dados.append(linha[coluna-1])

      return dados

   def limpar_planilha(self):
      """
      Limpa todos os dados da planilha.
      """
      for linha in self.planilha.iter_rows():
         for celula in linha:
            celula.value = None

      self.workbook.save(self.nome_planilha)
   
   def excluir_linha(self, nome:str, coluna:int):
      """
      Exclui a linha em que o parâmetro passado esta.

      Args:
         nome (str): O nome do dispositivo a ser excluído.
         coluna (int): coluna na qual o nome está

      Returns:
         bool: True se o dispositivo foi excluído com sucesso, False caso contrário.
      """
      linha_a_excluir = 1
      for linha in self.planilha.iter_rows(min_row=1, values_only=True):
         if linha[coluna] == nome:
            self.planilha.delete_rows(linha_a_excluir)
            self.workbook.save(self.nome_planilha)
            return True
         linha_a_excluir += 1
      return False


