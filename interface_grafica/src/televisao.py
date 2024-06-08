from src.objetos import Objeto

class Televisao (Objeto):

    def __init__ (self, nome:str, planilha:str) -> None:
        super().__init__(nome, planilha)
        self.canal = 1
        self.volume = 0
        self.ligado = False
        self.tipo = 'Televisor'
        self.dados_tv = [self.nome, self.tipo, self.canal, self.volume, self.ligado]

    def ligar (self) -> None:
        self.ligado = self.planilha.retorna_valor(self.nome, 5)
        if self.ligado == False:
            self.dados_tv [4] = True
        else:
            self.dados_tv[4] = False
        self.planilha.editar(self.dados_tv,4)

    def mudar_canal (self, novo_canal) -> None:
        self.dados_tv[2] = novo_canal
        self.planilha.editar(self.dados_tv,2)

    def mudar_volume (self, novo_volume) -> None:
        if novo_volume > 100:
            self.dados_tv[3] = 100
            self.planilha.editar(self.dados_tv,3)
            return
        if novo_volume < 0:
            self.dados_tv[3] = 0
            self.planilha.editar(self.dados_tv,3)
            return
        self.dados_tv[3] = novo_volume
        self.planilha.editar(self.dados_tv,3)
    
    def salvar(self) -> bool:
        if self.planilha.retorna_quantidade('Televisor') < 6:
            if not (self.planilha.verifica_se_objeto_existe(self.nome)):
                return super().salvar(self.dados_tv)
        else:
            return False
    
    def canal_atual(self) -> int:
        return self.planilha.retorna_valor(self.nome, 3)
    
    def volume_atual(self) -> int:
        return self.planilha.retorna_valor(self.nome, 4)
    
    def esta_ligado(self) -> bool:
        return self.planilha.retorna_valor(self.nome, 5)
    
    def excluir(self) -> bool:
        return self.planilha.excluir_dispositivo(self.nome)
# tv = Televisao ('Tv da cozinha')
# tv.ligar()
# tv.mudar_canal('Canal 3')
# tv.mudar_volume (10)
