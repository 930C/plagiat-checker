from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtWidgets import (QTableWidget, QTableWidgetItem, QHeaderView)
from PySide6.QtWidgets import *
from Qt.ui_frm_main import Ui_frm_main
import main as m
import sentenceSplitter as ss

class Frm_main(QMainWindow, Ui_frm_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_check.clicked.connect(self.check)
        self.progressBar.setValue(0)
        
    def check(self):
        #content = ss.splitter(self.te_input.toPlainText())
        plagiate = m.main(self.te_input.toPlainText(), self)

        self.tv_ergebnisse.setRowCount(len(plagiate))
        self.tv_ergebnisse.setColumnCount(2)
        self.tv_ergebnisse.setHorizontalHeaderLabels(["Satz", "Quelle"])
        self.tv_ergebnisse.setColumnWidth(0, 700)
        self.tv_ergebnisse.setColumnWidth(1, 250)

        for index, value in enumerate(plagiate):
            self.itemSatz = QTableWidgetItem(plagiate[index][0])
            self.tv_ergebnisse.setItem(index, 0, self.itemSatz)

            self.itemQuelle = QTableWidgetItem(plagiate[index][1])
            self.tv_ergebnisse.setItem(index, 1, self.itemQuelle)
   
    def progress(self, num):
        self.progressBar.setValue(num)

app = QApplication()
frm_main = Frm_main()
frm_main.show()
app.exec()