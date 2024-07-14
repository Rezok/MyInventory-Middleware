from Model.MainModel import MainModel
from View.MainView import MainView
from Controller.MainController import MainController

"""
        CURRENT_VERSION: 1.0
        AUTHOR: Jakub Pankiewicz
        DESCRIPTION: This is the main application class

        **CHANGELOG**
        12.07.2024 |1.0| - Create App python file
    """


def main():
    main_view = MainView()
    main_model = MainModel()
    main_controller = MainController(main_model, main_view)
    main_controller.start()


if __name__ == '__main__':
    main()

