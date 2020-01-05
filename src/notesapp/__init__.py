
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication
from notesapp.constants import HUMAN_APP_NAME
from notesapp.init import init_app_data_dir, init_app_db


def run(argv):

    init_app_data_dir()
    # init_app_db()

    from notesapp.log import LOGGER
    LOGGER.info(
        '======================================Notesapp starting up=======================================')

    # import imagius.settings
    # settings.load_settings()

    from notesapp.main_window import MainWindow

    app = QApplication(argv)
    app.setApplicationName(HUMAN_APP_NAME)
    w = MainWindow()

    # with open('styles/Aqua.qss', 'r') as stylesheet:
    #     qss = stylesheet.read()

    # w.setStyleSheet(qss)

    w.setWindowTitle('NotesApp')
    w.showMaximized()

    return app.exec_()
