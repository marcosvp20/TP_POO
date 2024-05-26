from src.objetos import Objeto

class Lampada(Objeto):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.brilho = 0
        self.tipo = 'lampada'
        self.dados_lampada = [self.nome, self.tipo, self.brilho, self.ligado]
        self.salvar(self.dados_lampada)

    def ligar(self) -> None:
        self.ligado = self.planilha.retorna_valor(self.nome, 4)
        if self.ligado == False:
            self.dados_lampada[3] = True
        else:
            self.dados_lampada[3] = False
        self.planilha.editar(self.dados_lampada)

    def aumentar_brilho(self, porcentagem:int) -> None:
        self.brilho = self.planilha.retorna_valor(self.nome, 3)
        if self.brilho < 100:
            if self.brilho + porcentagem > 100:
                self.dados_lampada[2] = 100
            else:
                self.dados_lampada[2] += porcentagem
        self.planilha.editar(self.dados_lampada)
        
    def diminuir_brilho(self, porcentagem:int) -> None:
        self.brilho = self.planilha.retorna_valor(self.nome, 3)
        if self.brilho > 0:
            if self.brilho - porcentagem < 0:
                self.dados_lampada[2] = 0
            else:
                self.dados_lampada[2] -= porcentagem
        self.planilha.editar(self.dados_lampada)
    
        
# lamp = Lampada('Lampada do quarto')
# lamp1 = Lampada('Lampada da sala')
# lamp.ligar()
# lamp.aumentar_brilho(30)
# lamp.aumentar_brilho(100)
