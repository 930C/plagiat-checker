from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtWidgets import (QTableWidget, QTableWidgetItem)
from Qt.ui_frm_main import Ui_frm_main
import main as m

class Frm_main(QMainWindow, Ui_frm_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.bt_check.clicked.connect(self.check)
 

app = QApplication()
frm_main = Frm_main()

frm_main.show()
app.exec()