from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from Qt.frm_main import Ui_frm_main

class Frm_main(QMainWindow, Ui_frm_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_check.clicked.connect(self.check)
        self.tv_ergebnisse.setItem(0,0, QTablewidgetItem("Name"))

    def check(self):
        print(self.te_input.toPlainText())

app = QApplication()
frm_main = Frm_main()

frm_main.show()
app.exec()