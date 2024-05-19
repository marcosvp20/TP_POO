from objetos import Objeto

class ArCondicionado(Objeto):
    
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.temperatura = 23
        self.dados_ar = [self.nome, self.temperatura, self.ligado]
        self.salvar()
    
    def salvar(self) -> None:
        self.planilha.salvar(self.dados_ar)
    
    def mudar_temperatura(self, temperatura) -> None:
        self.dados_ar[1] = temperatura
        self.planilha.editar(self.dados_ar)
        
    def ligar(self) -> None:
        self.dados_ar[2] = True
        self.planilha.editar(self.dados_ar)
    
ar = ArCondicionado('Ar da sala')
ar1 = ArCondicionado('Ar do quarto')
ar.ligar()
ar.mudar_temperatura(18)