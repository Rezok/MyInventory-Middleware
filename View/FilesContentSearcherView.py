import tkinter
from tkinter import *
from tkinter import ttk


class FilesContentSearcherView(ttk.Frame):
    """
        CURRENT_VERSION: 1.0
        AUTHOR: Jakub Pankiewicz
        DESCRIPTION: This class represent View of FilesContentSearcher.

        **CHANGELOG**
        12.07.2024 |1.0| - Create View
    """

    def __init__(self, parent):
        super().__init__(parent)

        # Icons
        files_explorer_image = PhotoImage(file="Images/file-explorer-icon.png")
        search_image = PhotoImage(file="Images/search-icon.png")

        # Styles configuration
        self.label_style = ttk.Style().configure("TLabel", padding=(5, 0, 0, 0))
        self.entry_style = ttk.Style().configure("TEntry", padding=(5, 0, 0, 0), borderwidth=10, bg='green')

        # View elements
        self.path_value = ttk.Entry(self, style="TEntry", font=("Arial", 12))
        self.path_value.insert(0, "D:/AMR/MyINV")
        self.path_button = ttk.Button(self, image=files_explorer_image)
        self.search_button = ttk.Button(self, image=search_image)
        self.search_button.image = search_image
        self.path_button.image = files_explorer_image
        self.separator = ttk.Separator(self, orient='horizontal')

        self.value_label = ttk.Label(self, text='Search value:', style="TLabel", font=("Arial", 12))
        self.input_value = ttk.Entry(self, font=("Arial", 10), style="TEntry")
        self.servers_list_label = ttk.Label(self, text='Server:', style="TLabel", font=("Arial", 12))
        self.servers_list = ttk.Combobox(self, font=("Arial", 10), state='readonly')
        self.separator2 = ttk.Separator(self, orient='horizontal')

        self.result_text = ttk.Treeview(self, columns=("File Name", "Modify Date", "Created Date"), show="headings")
        self.result_text.heading("0", text="File Name")
        self.result_text.column("0", width=400, anchor=tkinter.CENTER)
        self.result_text.heading("1", text="Modify Date")
        self.result_text.heading("2", text="Created Date")

        # View elements configuration
        self.path_value.place(x=5, y=5, width=800, height=40)
        self.path_button.place(x=809, y=5, width=40, height=40)
        self.search_button.place(x=764, y=6, width=40, height=38)
        self.separator.place(x=0, y=50, width=854, height=1)

        self.value_label.place(x=0, y=56, width=105, height=40)
        self.input_value.place(x=110, y=61, width=150, height=30)
        self.servers_list_label.place(x=265, y=56, width=60, height=40)
        self.servers_list.place(x=330, y=61, width=150, height=30)
        self.separator2.place(x=0, y=101, width=854, height=1)

        self.result_text.place(x=5, y=106, width=844, height=369)
        # self.separator.place(x=0, y=45, width=400, height=1)

        # set empty controller
        self.controller = None
