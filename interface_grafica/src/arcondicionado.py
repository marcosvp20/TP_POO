from src.objetos import Objeto

class ArCondicionado(Objeto):
    
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.temperatura = 23
        self.tipo = 'A/C'
        self.dados_ar = [self.nome, self.tipo, self.temperatura, self.ligado]
        # self.salvar(self.dados_ar)

    def mudar_temperatura(self, temperatura) -> None:
        self.dados_ar[2] = temperatura
        self.planilha.editar(self.dados_ar)
        
    def ligar(self) -> None:
        self.dados_ar[3] = True
        self.planilha.editar(self.dados_ar)
    
    def salvar(self):
        if self.planilha.retorna_quantidade('A/C') < 6:
            return super().salvar(self.dados_ar)
        return False
    
# ar = ArCondicionado('Ar da sala')
# ar1 = ArCondicionado('Ar do quarto')
# ar.ligar()
# ar.mudar_temperatura(18)