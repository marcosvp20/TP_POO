import customtkinter as ctk
from PIL import Image
from interfacedispositivos.botao_disp import Botao
from interfacedispositivos.InterfaceNewDisp import InterfaceNewDisp
import os
from interfacedispositivos.b_dinamico_disp import BotaoDinamicoDisp
from src.frame import Frame

class interfaceDispositivos:
    def __init__(self, janela) -> None:
        """
        Classe responsável por criar a interface de dispositivos.
        """
        self.janela = janela
        
    def criaframe(self) -> None:
        """
        Cria o frame da interface de dispositivos.
        """
        self.frame_dispositivos = Frame(self.janela, 'Dispositivos: ', '').frame
        
    def executar(self) -> None:
        """
        Executa a interface de dispositivos.
        """
        self.criaframe()
        InterfaceNewDisp(self.janela)
        bd = BotaoDinamicoDisp(self.frame_dispositivos)
        bd.insere_botao_add()
    
    def atualizar(self) -> None:
        """
        Atualiza a interface de dispositivos.
        """
        self.frame_dispositivos.update()
        