import customtkinter as ctk

class Switch:
    """
    Classe Switch para criar um switch personalizado usando customtkinter.

    Atributos:
        __switch (ctk.CTkSlider): O switch personalizado.

    Métodos:
        __init__(frame, comando): Inicializa um switch.
        select(): Seleciona o switch.
    """

    def __init__(self, frame: ctk.CTkFrame, comando: callable, padx:int, pady:int) -> None:
        """
        Inicializa um novo switch.

        Parâmetros:
            frame (ctk.CTkFrame): O frame onde o switch será adicionado.
            comando (callable): A função que será chamada quando o valor do switch mudar.
        """
        self.switch = ctk.CTkSwitch(frame,
                                text="",
                                command=comando,
                                width=85,
                                height=40,
                                fg_color="gray",
                                progress_color="#348faa",
                                button_color="black",
                                corner_radius=35,
                                bg_color='white',
                                switch_height=40,
                                switch_width=85)
        self.switch.place(x=padx, y=pady)
        
        # if set:
        #     self.switch.select()
