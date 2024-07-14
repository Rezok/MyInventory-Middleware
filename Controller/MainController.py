from Controller.FilesContentSearcherController import FilesContentSearcherController
from Controller.HomeController import HomeController
from Model.MainModel import MainModel
from View import MainView


class MainController:
    """
        CURRENT_VERSION: 1.0
        AUTHOR: Jakub Pankiewicz
        DESCRIPTION: This class represent MainController of application.

        **CHANGELOG**
        12.07.2024 |1.0| - Create MainController implementation.
    """
    def __init__(self, main_model: MainModel, main_view: MainView):
        self.model = main_model
        self.view = main_view
        self.home_controller = HomeController(self.model, self.view)
        self.fcs_controller = FilesContentSearcherController(self.model, self.view)

    def start(self):
        self.view.start_mainloop()
