from abc import ABC, abstractmethod
import customtkinter as ctk

class ISlider(ABC):

    @abstractmethod
    def __init__(self, frame: ctk.CTkFrame, inicio: int, fim: int, comando: callable, posicao_atual: callable, posx:int, posy:int) -> None:
        pass
        