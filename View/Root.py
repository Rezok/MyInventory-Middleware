import tkinter


class Root(tkinter.Tk):
    """
        CURRENT_VERSION: 1.0
        AUTHOR: Jakub Pankiewicz
        DESCRIPTION: This Root windows class of application.

        **CHANGELOG**
        12.07.2024 |1.0| - Create Root windows basic configuration.
    """
    def __init__(self):
        super().__init__()

        self.version = "0.0.1"
        self.title(f"MyInventoryMiddleware {self.version}")
        self.geometry("854x480")
        self.resizable(False, False)
