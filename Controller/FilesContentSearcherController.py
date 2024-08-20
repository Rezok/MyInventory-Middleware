from tkinter import filedialog

from Model.MainModel import MainModel
from View.MainView import MainView


class FilesContentSearcherController:
    """
        CURRENT_VERSION: 1.0
        AUTHOR: Jakub Pankiewicz
        DESCRIPTION: This class represent controller of FilesContentSearcherView.

        **CHANGELOG**
        12.07.2024 |1.0| - Create FileContentSearcherView implementation
    """
    def __init__(self, model: MainModel, view: MainView):
        self.model = model
        self.view = view
        self.frame = self.view.frames["fcs_view"]
        self._bind()

    def _bind(self):
        self.frame.path_button.config()
        self.frame.servers_list["values"] = self.model.file_content_searcher_model.get_servers()
        self.frame.servers_list.current(0)

    def open_file_explorer(self):
        path = filedialog.askdirectory(title="Select Folder")
        print(path)