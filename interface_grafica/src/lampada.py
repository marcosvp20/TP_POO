from src.objetos import Objeto

class Lampada(Objeto):
    def __init__(self, nome, planilha:str) -> None:
        super().__init__(nome, planilha)
        self.brilho = 0
        self.tipo = 'Lâmpada'
        self.dados_lampada = [self.nome, self.tipo, self.brilho, self.ligado]
        
    def ligar(self) -> None:
        self.ligado = self.planilha.retorna_valor(self.nome, 4)
        if self.ligado == False:
            self.dados_lampada[3] = True
        else:
            self.dados_lampada[3] = False
        self.planilha.editar(self.dados_lampada,3)
        
    def mudar_brilho(self, porcentagem:int) -> None:
        self.dados_lampada[2] = porcentagem
        self.planilha.editar(self.dados_lampada,2)
    
    def brilho_atual(self) -> int:
        return self.planilha.retorna_valor(self.nome, 3)
    
    def esta_ligado(self) -> bool:
        return self.planilha.retorna_valor(self.nome, 4)
    
    def excluir(self) -> bool:
        return self.planilha.excluir_dispositivo(self.nome)

    def salvar(self) -> bool:
        if self.planilha.retorna_quantidade('Lâmpada') < 6:
            if not (self.planilha.verifica_se_objeto_existe(self.nome)):
                return super().salvar(self.dados_lampada)
        else:
            return False
        
