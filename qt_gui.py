from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtWidgets import (QTableWidget, QTableWidgetItem)
from Qt.frm_main import Ui_frm_main
import main as m

class Frm_main(QMainWindow, Ui_frm_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_check.clicked.connect(self.check)


    def check(self):
        plagiate = m.main(self.te_input.toPlainText())

        self.tv_ergebnisse.setRowCount(len(plagiate))
        self.tv_ergebnisse.setColumnCount(2)
        self.tv_ergebnisse.setHorizontalHeaderLabels(["Satz", "Quelle"])

        for index, value in enumerate(plagiate):
            self.itemSatz = QTableWidgetItem(plagiate[index][0])
            self.tv_ergebnisse.setItem(index, 0, self.itemSatz)

            self.itemQuelle = QTableWidgetItem(plagiate[index][1])
            self.tv_ergebnisse.setItem(index, 1, self.itemQuelle)
 

app = QApplication()
frm_main = Frm_main()

frm_main.show()
app.exec()