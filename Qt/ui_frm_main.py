# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_mainUSQwmi.ui'
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
        frm_main.resize(1200, 800)
        font = QFont()
        font.setPointSize(11)
        frm_main.setFont(font)
        frm_main.setToolButtonStyle(Qt.ToolButtonIconOnly)
        frm_main.setTabShape(QTabWidget.Rounded)
        self.action_ffnen = QAction(frm_main)
        self.action_ffnen.setObjectName(u"action_ffnen")
        self.actionBeenden = QAction(frm_main)
        self.actionBeenden.setObjectName(u"actionBeenden")
        self.centralwidget = QWidget(frm_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setInvertedAppearance(False)

        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 1)

        self.lb_ergebnisse = QLabel(self.centralwidget)
        self.lb_ergebnisse.setObjectName(u"lb_ergebnisse")
        font1 = QFont()
        font1.setPointSize(20)
        self.lb_ergebnisse.setFont(font1)
        self.lb_ergebnisse.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_ergebnisse, 6, 0, 1, 1)

        self.lb_plagiatChecker = QLabel(self.centralwidget)
        self.lb_plagiatChecker.setObjectName(u"lb_plagiatChecker")
        self.lb_plagiatChecker.setEnabled(True)
        font2 = QFont()
        font2.setPointSize(28)
        self.lb_plagiatChecker.setFont(font2)
        self.lb_plagiatChecker.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_plagiatChecker, 0, 0, 1, 1, Qt.AlignHCenter)

        self.bt_check = QPushButton(self.centralwidget)
        self.bt_check.setObjectName(u"bt_check")
        font3 = QFont()
        font3.setFamily(u"Noto Sans Display Bold")
        font3.setPointSize(24)
        self.bt_check.setFont(font3)
        self.bt_check.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_check.setAutoFillBackground(False)
        self.bt_check.setStyleSheet(u"background-color: rgb(0,255,0)")

        self.gridLayout.addWidget(self.bt_check, 4, 0, 1, 1, Qt.AlignHCenter)

        self.te_input = QPlainTextEdit(self.centralwidget)
        self.te_input.setObjectName(u"te_input")
        font4 = QFont()
        font4.setPointSize(12)
        self.te_input.setFont(font4)

        self.gridLayout.addWidget(self.te_input, 1, 0, 1, 1)

        self.tv_ergebnisse = QTableWidget(self.centralwidget)
        if (self.tv_ergebnisse.columnCount() < 2):
            self.tv_ergebnisse.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tv_ergebnisse.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tv_ergebnisse.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tv_ergebnisse.setObjectName(u"tv_ergebnisse")
        self.tv_ergebnisse.setFont(font)
        self.tv_ergebnisse.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.gridLayout.addWidget(self.tv_ergebnisse, 7, 0, 1, 1)

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
        self.bt_check.clicked.connect(self.progressBar.reset)

        QMetaObject.connectSlotsByName(frm_main)
    # setupUi

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"Plagiat Checker v1", None))
        self.action_ffnen.setText(QCoreApplication.translate("frm_main", u"\u00d6ffnen", None))
        self.actionBeenden.setText(QCoreApplication.translate("frm_main", u"Beenden", None))
        self.progressBar.setFormat("")
        self.lb_ergebnisse.setText(QCoreApplication.translate("frm_main", u"Ergebnisse", None))
        self.lb_plagiatChecker.setText(QCoreApplication.translate("frm_main", u"Plagiat Checker", None))
        self.bt_check.setText(QCoreApplication.translate("frm_main", u"Check", None))
        self.te_input.setPlainText(QCoreApplication.translate("frm_main", u"Hier Text eingeben...", None))
        ___qtablewidgetitem = self.tv_ergebnisse.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("frm_main", u"Satz", None));
        ___qtablewidgetitem1 = self.tv_ergebnisse.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("frm_main", u"Quelle", None));
        self.menuDatei.setTitle(QCoreApplication.translate("frm_main", u"Datei", None))
    # retranslateUi

