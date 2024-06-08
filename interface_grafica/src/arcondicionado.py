from src.objetos import Objeto

class ArCondicionado(Objeto):
    
    def __init__(self, nome, planilha:str) -> None:
        super().__init__(nome, planilha)
        self.temperatura = 23
        self.tipo = 'A/C'
        self.dados_ar = [self.nome, self.tipo, self.temperatura, self.ligado]

    def mudar_temperatura(self, temperatura) -> None:
        self.dados_ar[2] = temperatura
        self.planilha.editar(self.dados_ar,2)
        
    def ligar(self) -> None:
        self.dados_ar[3] = True
        self.planilha.editar(self.dados_ar,3)

    def desligar(self) -> None:
        self.dados_ar[3] = False
        self.planilha.editar(self.dados_ar,3)
    
    def salvar(self):
        if (self.planilha.retorna_quantidade('A/C') < 6):
            if not (self.planilha.verifica_se_objeto_existe(self.nome)):
                return super().salvar(self.dados_ar)
        return False
    
    def temperatura_atual(self) -> int:
        return self.planilha.retorna_valor(self.nome,3)
    
    def esta_ligado(self) -> bool:
        return self.planilha.retorna_valor(self.nome,4)
    
    def excluir(self) -> bool:
        return self.planilha.excluir_dispositivo(self.nome)
    
# ar = ArCondicionado('Ar da sala')
# ar1 = ArCondicionado('Ar do quarto')
# ar.ligar()
# ar.mudar_temperatura(18)