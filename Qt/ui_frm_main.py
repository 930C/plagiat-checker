# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_mainxBxeQh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_frm_main(object):
    def setupUi(self, frm_main):
        if not frm_main.objectName():
            frm_main.setObjectName(u"frm_main")
        frm_main.resize(965, 683)
        font = QFont()
        font.setPointSize(11)
        frm_main.setFont(font)
        self.action_ffnen = QAction(frm_main)
        self.action_ffnen.setObjectName(u"action_ffnen")
        self.actionBeenden = QAction(frm_main)
        self.actionBeenden.setObjectName(u"actionBeenden")
        self.centralwidget = QWidget(frm_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_plagiatChecker = QLabel(self.centralwidget)
        self.lb_plagiatChecker.setObjectName(u"lb_plagiatChecker")
        self.lb_plagiatChecker.setBaseSize(QSize(2, 0))
        font1 = QFont()
        font1.setFamily(u"Noto Sans Display Bold")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(False)
        # font1.setWeight(75)
        self.lb_plagiatChecker.setFont(font1)
        self.lb_plagiatChecker.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_plagiatChecker, 0, 0, 1, 1, Qt.AlignHCenter)

        self.te_input = QPlainTextEdit(self.centralwidget)
        self.te_input.setObjectName(u"te_input")
        self.te_input.setBaseSize(QSize(2, 0))
        font2 = QFont()
        font2.setPointSize(12)
        self.te_input.setFont(font2)

        self.gridLayout.addWidget(self.te_input, 1, 0, 1, 1)

        self.lb_ergebnisse = QLabel(self.centralwidget)
        self.lb_ergebnisse.setObjectName(u"lb_ergebnisse")
        self.lb_ergebnisse.setBaseSize(QSize(2, 0))
        font3 = QFont()
        font3.setPointSize(20)
        self.lb_ergebnisse.setFont(font3)
        self.lb_ergebnisse.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_ergebnisse, 5, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setBaseSize(QSize(2, 0))
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 1)

        self.bt_check = QPushButton(self.centralwidget)
        self.bt_check.setObjectName(u"bt_check")
        self.bt_check.setBaseSize(QSize(1, 1))
        self.bt_check.setFont(font1)
        self.bt_check.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_check.setAutoFillBackground(False)
        self.bt_check.setStyleSheet(u"background-color: green;\n"
"text-align: center;")

        self.gridLayout.addWidget(self.bt_check, 2, 0, 1, 1, Qt.AlignHCenter)

        self.tv_ergebnisse = QTableWidget(self.centralwidget)
        self.tv_ergebnisse.setObjectName(u"tv_ergebnisse")
        self.tv_ergebnisse.setBaseSize(QSize(2, 0))
        font4 = QFont()
        font4.setPointSize(14)
        self.tv_ergebnisse.setFont(font4)

        self.gridLayout.addWidget(self.tv_ergebnisse, 6, 0, 1, 1)

        frm_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 965, 34))
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
        # self.bt_check.clicked.connect(self.bt_check.click)

        QMetaObject.connectSlotsByName(frm_main)
    # setupUi

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"MainWindow", None))
        self.action_ffnen.setText(QCoreApplication.translate("frm_main", u"\u00d6ffnen", None))
        self.actionBeenden.setText(QCoreApplication.translate("frm_main", u"Beenden", None))
        self.lb_plagiatChecker.setText(QCoreApplication.translate("frm_main", u"Plagiat Checker", None))
        self.te_input.setPlainText(QCoreApplication.translate("frm_main", u"Hier Text eingeben...", None))
        self.lb_ergebnisse.setText(QCoreApplication.translate("frm_main", u"Ergebnisse", None))
        self.bt_check.setText(QCoreApplication.translate("frm_main", u"Check", None))
        self.menuDatei.setTitle(QCoreApplication.translate("frm_main", u"Datei", None))
    # retranslateUi

