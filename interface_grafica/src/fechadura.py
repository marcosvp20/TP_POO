from src.objetos import Objeto

class Fechadura(Objeto):
    
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.tipo = 'fechadura'
        self.trancado = False
        
        self.dados_fechadura = [self.nome, self.tipo, self.trancado]
        self.salvar(self.dados_fechadura)
        
    def trancar(self) -> None:
        self.dados_fechadura[2] = True
        self.planilha.editar(self.dados_fechadura)
    
    def destrancar(self) -> None:
        self.dados_fechadura[2] = False
        self.planilha.editar(self.dados_fechadura)
    