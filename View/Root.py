import tkinter


class Root(tkinter.Tk):
    """
        CURRENT_VERSION: 1.0.1
        AUTHOR: Jakub Pankiewicz
        DESCRIPTION: This Root windows class of application.

        **CHANGELOG**
        12.07.2024 |1.0| - Create Root windows basic configuration.
        14.07.2024 |1.0.1| - Add App Menu
    """

    def __init__(self):
        super().__init__()

        self.version = "0.0.2"
        self.title(f"MyInventoryMiddleware {self.version}")
        self.geometry("854x480")
        self.resizable(False, False)

        self.menu = tkinter.Menu(self)
        self.app_menu = tkinter.Menu(self.menu, tearoff=0)
