from tkinter import Menu
from View.FilesContentSearcherView import FilesContentSearcherView
from View.HomeView import HomeView
from View.Root import Root


class MainView:
    """
        CURRENT_VERSION: 1.0.1
        AUTHOR: Jakub Pankiewicz
        DESCRIPTION: This class represent MainView of application. It provides frame change system.

        **CHANGELOG**
        12.07.2024 |1.0| - Create MainView implementation.
        14.07.2024 |1.0.1| - Add back_home and generate_list_menu function to generate menu list and back to home screen
            function.
    """
    def __init__(self):
        self.root = Root()

        self.frames = {}

        self._add_frame(HomeView, "home")
        self._add_frame(FilesContentSearcherView, "fcs_view")

        self.current_frame = self.frames["home"]
        self.current_frame.pack(fill='both', expand='True')

        self.generate_list_menu()

    def _add_frame(self, frame, name: str):
        self.frames[name] = frame(self.root)

    def switch(self, name: str):
        new_frame = self.frames[name]
        self.current_frame.pack_forget()
        self.current_frame = new_frame
        self.current_frame.pack(fill='both', expand='True')

    def start_mainloop(self):
        self.root.mainloop()

    def back_home(self):
        self.current_frame.pack_forget()
        self.current_frame = self.frames["home"]
        self.current_frame.pack(fill='both', expand='True')

    def generate_list_menu(self):
        self.root.app_menu.add_command(label="Home Screen", command=self.back_home)
        self.root.menu.add_cascade(label="Menu", menu=self.root.app_menu)
        self.root.config(menu=self.root.menu)
