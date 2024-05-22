from objetos import Objeto

class Caixa_de_som(Objeto):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.volume = 0
        self.tipo = 'alto falante'
        self.musica = None
        self.pausado = False
        self.dados_caixa = [self.nome, self.tipo,  self.ligado, self.volume, self.musica, self.pausado]
        self.salvar(self.dados_caixa)
        
        
    def ligar(self) -> None:
        self.ligado = self.planilha.retorna_valor(self.nome, 3)
        if self.ligado == False:
            self.dados_caixa[2] = True
        else:
            self.dados_caixa[2] = False
        self.planilha.editar(self.dados_caixa)
        
    def mudar_volume(self, volume:int) -> None:
        self.dados_caixa[3] = volume
        self.planilha.editar(self.dados_caixa)
    
    def mudar_musica(self, musica:str) -> None:
        self.dados_caixa[4] = musica
        self.planilha.editar(self.dados_caixa)
    
    def pausar_musica(self) -> None:
        if self.planilha.retorna_valor(self.nome, 6):
            self.dados_caixa[5] = False
        else:
            self.dados_caixa[5] = True
        self.planilha.editar(self.dados_caixa)
            
    
caixa = Caixa_de_som('Alexa')
caixa.ligar()
caixa.mudar_volume(50)
caixa.mudar_musica('Leo Santana')
caixa.pausar_musica()
