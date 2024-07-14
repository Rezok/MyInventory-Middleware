from View.FilesContentSearcherView import FilesContentSearcherView
from View.HomeView import HomeView
from View.Root import Root


class MainView:
    """
        CURRENT_VERSION: 1.0
        AUTHOR: Jakub Pankiewicz
        DESCRIPTION: This class represent MainView of application. It provides frame change system.

        **CHANGELOG**
        12.07.2024 |1.0| - Create MainView implementation.
    """
    def __init__(self):
        self.root = Root()

        self.frames = {}

        self._add_frame(HomeView, "home")
        self._add_frame(FilesContentSearcherView, "fcs_view")

        self.current_frame = self.frames["home"]
        self.current_frame.pack(fill='both', expand='True')

    def _add_frame(self, frame, name: str):
        self.frames[name] = frame(self.root)

    def switch(self, name: str):
        new_frame = self.frames[name]
        self.current_frame.pack_forget()
        self.current_frame = new_frame
        self.current_frame.pack(fill='both', expand='True')

    def start_mainloop(self):
        self.root.mainloop()
