
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QWindow, QIcon, QPixmap
from noteslot.constants import HUMAN_APP_NAME
from noteslot.init import init_app_data_dir, init_app_db
from noteslot import noteslot_rc


def run(argv):

    init_app_data_dir()
    init_app_db()

    from noteslot.log import LOGGER
    LOGGER.info(
        '======================================Noteslot starting up=======================================')

    import noteslot.settings
    settings.load_settings()

    from noteslot.main_window import MainWindow

    app = QApplication(argv)
    app.setApplicationName(HUMAN_APP_NAME)
    w = MainWindow()
    w.setWindowIcon(QIcon(QPixmap(':/icons/resources/icons/noteslot.png')))
    w.setWindowTitle('noteslot')
    w.show()

    return app.exec_()
