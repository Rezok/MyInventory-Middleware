from tkinter.ttk import Frame, Button


class HomeView(Frame):
    """
        CURRENT_VERSION: 1.0
        AUTHOR: Jakub Pankiewicz
        DESCRIPTION: This class represent home application view. It provides canvas to go to specific module of
            application.

        **CHANGELOG**
        12.07.2024 |1.0| - Create HomeView implementation.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fcs_button = Button(self, text="Files Content Searcher")
        self.fcs_button.place(x=5, y=5, width=150, height=150)
