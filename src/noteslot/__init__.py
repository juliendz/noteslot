
from PySide2 import QtCore
from PySide2.QtCore import QLockFile
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtGui import QWindow, QIcon, QPixmap
from noteslot.constants import HUMAN_APP_NAME, LOCK_FILE
from noteslot.init import init_app_data_dir, init_app_db
from noteslot import noteslot_rc


def run(argv):

    app = QApplication(argv)

    ##########################################################
    # A crude check to prevent multiple instances from running
    ##########################################################
    lock_file = QLockFile(LOCK_FILE)
    if not lock_file.tryLock(100):
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Warning)
        mb.setText("The application is already running.")
        mb.exec_()
        return 1

    init_app_data_dir()
    init_app_db()

    from noteslot.log import LOGGER

    import noteslot.settings
    settings.load_settings()

    from noteslot.main_window import MainWindow

    app.setApplicationName(HUMAN_APP_NAME)
    w = MainWindow()
    w.setWindowIcon(QIcon(QPixmap(':/icons/resources/icons/noteslot.png')))
    w.setWindowTitle('noteslot')

    from noteslot.notes import Notes
    nts = Notes()
    w.open_pinned_notes()
    if nts.get_pinned_notes_count() == 0:
        w.show()

    return app.exec_()
