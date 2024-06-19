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

    def __init__(self, frame: ctk.CTkFrame, comando: callable, set: bool) -> None:
        """
        Inicializa um novo switch.

        Parâmetros:
            frame (ctk.CTkFrame): O frame onde o switch será adicionado.
            comando (callable): A função que será chamada quando o valor do switch mudar.
        """
        self.__off_label = ctk.CTkLabel(frame,
                                 text="OFF",
                                 font=('League Spartan', 30),
                                 fg_color='white',
                                 bg_color='transparent')
        self.__off_label.place(x=100, y=190)
        
        self.__switch = ctk.CTkSwitch(frame,
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
        self.__switch.place(x=183, y=195)
        
        self.__on_label = ctk.CTkLabel(frame,
                                text="ON",
                                font=('League Spartan', 30),
                                fg_color='white',
                                bg_color='transparent')
        self.__on_label.place(x=305, y=190)

        if set:
            self.__switch.select()

    # def select(self) -> None:
    #     self.__switch.select()