from PySide2 import QtWidgets
from Ui_MainWindow import Ui_MainWindow
import ui_fuzzy_assigner
import sys

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = ui_fuzzy_assigner.Ui_fuzzy_assigner_window()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()