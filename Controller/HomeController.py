from Model.MainModel import MainModel
from View.MainView import MainView


class HomeController:
    """
        CURRENT_VERSION: 1.0
        AUTHOR: Jakub Pankiewicz
        DESCRIPTION: This class represents HomeView controller.

        **CHANGELOG**
        12.07.2024 |1.0| - Create HomeView Controller
    """
    def __init__(self, model: MainModel, view: MainView):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self):
        self.frame.fcs_button.config(command=self.go_to_fcs_view)

    def go_to_fcs_view(self):
        self.view.switch("fcs_view")
