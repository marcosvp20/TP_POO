from objetos import Objeto

class Caixa_de_som(Objeto):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.volume = 0
        self.musica = None
        self.pausado = False
        self.dados_caixa = [self.nome, self.ligado, self.volume, self.musica, self.pausado]
        self.salvar()
        
        
    def ligar(self) -> None:
        self.ligado = self.planilha.retorna_valor(self.nome, 2)
        if self.ligado == False:
            self.dados_caixa[1] = True
        else:
            self.dados_caixa[1] = False
        self.planilha.editar(self.dados_caixa)
        
    def salvar(self) -> None:
        self.planilha.salvar(self.dados_caixa)
    
    def mudar_volume(self, volume:int) -> None:
        self.dados_caixa[2] = volume
        self.planilha.editar(self.dados_caixa)
    
    def mudar_musica(self, musica:str) -> None:
        self.dados_caixa[3] = musica
        self.planilha.editar(self.dados_caixa)
    
    def pausar_musica(self) -> None:
        if self.planilha.retorna_valor(self.nome, 5):
            self.dados_caixa[4] = False
        else:
            self.dados_caixa[4] = True
        self.planilha.editar(self.dados_caixa)
            
    
caixa = Caixa_de_som('Alexa')
caixa.ligar()
caixa.mudar_volume(50)
caixa.mudar_musica('Leo Santana')
caixa.pausar_musica()
