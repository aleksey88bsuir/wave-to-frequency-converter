from email.mime import application
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from user_interface import Ui_MainWindow


class Currency_conv(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Конвертер волн в частоты и обратно")
        self.setWindowIcon(QIcon("pictures/icons8-ок-16.png"))

app = QtWidgets.QApplication([])
application = Currency_conv()
application.show()

sys.exit(app.exec())
