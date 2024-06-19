import customtkinter as ctk

class Slider:
    """
    Classe Slider para criar um controle deslizante personalizado usando customtkinter.

    Atributos:
        __slider (ctk.CTkSlider): O controle deslizante personalizado.

    Métodos:
        __init__(frame, inicio, fim, comando, posicao_atual): Inicializa um novo controle deslizante.
        retorna_slider(): Retorna o controle deslizante.
    """

    def __init__(self, frame: ctk.CTkFrame, inicio: int, fim: int, comando: callable, posicao_atual: callable, posx:int, posy:int) -> None:
        """
        Inicializa um novo controle deslizante (Slider).

        Parâmetros:
            frame (ctk.CTkFrame): O frame onde o controle deslizante será adicionado.
            inicio (int): O valor inicial do controle deslizante.
            fim (int): O valor final do controle deslizante.
            comando (callable): A função que será chamada quando o valor do controle deslizante mudar.
            posicao_atual (callable): A função que retorna a posição inicial do controle deslizante.
            posx (int): A posição x (horizontal) do controle deslizante no frame.
            posy (int): A posição y (vertical) do controle deslizante no frame.
        """
        self.__slider = ctk.CTkSlider(frame,
                                      from_=inicio, to=fim,
                                      command=lambda value: comando(value),
                                      bg_color='#EDF4F9',
                                      fg_color='gray',
                                      progress_color='#348faa',
                                      button_color='black',
                                      width=270,
                                      height=20)
        self.__slider.set(posicao_atual())
        self.__slider.place(x=posx, y=posy)
