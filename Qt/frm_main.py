# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        if not frm_main.objectName():
            frm_main.setObjectName(u"frm_main")
        frm_main.resize(1200, 800)
        font = QFont()
        font.setPointSize(11)
        frm_main.setFont(font)
        self.action_ffnen = QAction(frm_main)
        self.action_ffnen.setObjectName(u"action_ffnen")
        self.actionBeenden = QAction(frm_main)
        self.actionBeenden.setObjectName(u"actionBeenden")
        self.centralwidget = QWidget(frm_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lb_plagiatChecker = QLabel(self.centralwidget)
        self.lb_plagiatChecker.setObjectName(u"lb_plagiatChecker")
        self.lb_plagiatChecker.setGeometry(QRect(0, 20, 1191, 41))
        font1 = QFont()
        font1.setPointSize(24)
        self.lb_plagiatChecker.setFont(font1)
        self.lb_plagiatChecker.setAlignment(Qt.AlignCenter)
        self.lb_ergebnisse = QLabel(self.centralwidget)
        self.lb_ergebnisse.setObjectName(u"lb_ergebnisse")
        self.lb_ergebnisse.setGeometry(QRect(0, 440, 1201, 41))
        self.lb_ergebnisse.setFont(font1)
        self.lb_ergebnisse.setAlignment(Qt.AlignCenter)
        self.tv_ergebnisse = QTableWidget(self.centralwidget)
        self.tv_ergebnisse.setObjectName(u"tv_ergebnisse")
        self.tv_ergebnisse.setGeometry(QRect(10, 490, 1181, 261))
        self.te_input = QPlainTextEdit(self.centralwidget)
        self.te_input.setObjectName(u"te_input")
        self.te_input.setGeometry(QRect(10, 60, 1181, 311))
        self.bt_check = QPushButton(self.centralwidget)
        self.bt_check.setObjectName(u"bt_check")
        self.bt_check.setGeometry(QRect(510, 380, 181, 41))
        font2 = QFont()
        font2.setPointSize(17)
        self.bt_check.setFont(font2)
        frm_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 23))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        frm_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_main)
        self.statusbar.setObjectName(u"statusbar")
        frm_main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menuDatei.addAction(self.action_ffnen)
        self.menuDatei.addAction(self.actionBeenden)

        self.retranslateUi(frm_main)

        QMetaObject.connectSlotsByName(frm_main)
    # setupUi

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"MainWindow", None))
        self.action_ffnen.setText(QCoreApplication.translate("frm_main", u"\u00d6ffnen", None))
        self.actionBeenden.setText(QCoreApplication.translate("frm_main", u"Beenden", None))
        self.lb_plagiatChecker.setText(QCoreApplication.translate("frm_main", u"Plagiat Checker", None))
        self.lb_ergebnisse.setText(QCoreApplication.translate("frm_main", u"Ergebnisse", None))
        self.bt_check.setText(QCoreApplication.translate("frm_main", u"Check", None))
        self.menuDatei.setTitle(QCoreApplication.translate("frm_main", u"Datei", None))
    # retranslateUi

