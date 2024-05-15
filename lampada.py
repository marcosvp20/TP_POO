from objetos import Objeto
from planilha import Planilha

class Lampada(Objeto):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.ligada = False
        self.brilho = 0
        self.dados_lampada = [self.nome, self.brilho, self.ligada]
        self.salvar()

    def ligar(self):
        self.ligada = self.planilha.retorna_valor(self.nome, 3)
        if self.ligada == False:
            self.ligada = True
        else:
            self.ligada = False
        self.planilha.editar(self.nome, 3, self.ligada)

    def aumentar_brilho(self, porcentagem):
        self.brilho = self.planilha.retorna_valor(self.nome, 2)
        if self.brilho < 100:
            if self.brilho + porcentagem > 100:
                self.brilho = 100
            else:
                self.brilho += porcentagem
        self.planilha.editar(self.nome, 2, self.brilho)
        
    def diminuir_brilho(self, porcentagem):
        self.brilho = self.planilha.retorna_valor(self.nome, 2)
        if self.brilho > 0:
            if self.brilho - porcentagem < 0:
                self.brilho = 0
            else:
                self.brilho -= porcentagem
        self.planilha.editar(self.nome, 2, self.brilho)
    
    def salvar(self):
        self.planilha.salvar(self.dados_lampada)

lamp = Lampada('Lampada do quarto')
lamp.aumentar_brilho(70)
lamp.ligar()
lamp.diminuir_brilho(30)
