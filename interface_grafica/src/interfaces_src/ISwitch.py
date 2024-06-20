from abc import ABC, abstractmethod
import customtkinter as ctk

class ISwitch(ABC):

    @abstractmethod
    def __init__(self, frame: ctk.CTkFrame, comando: callable, padx:int, pady:int) -> None:
        pass