# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledOLPLbA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import 1_r

class Ui_fuzzy_assigner_window(object):
    def setupUi(self, fuzzy_assigner_window):
        if not fuzzy_assigner_window.objectName():
            fuzzy_assigner_window.setObjectName(u"fuzzy_assigner_window")
        fuzzy_assigner_window.resize(1030, 839)
        self.actionLoad = QAction(fuzzy_assigner_window)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionSave = QAction(fuzzy_assigner_window)
        self.actionSave.setObjectName(u"actionSave")
        self.centralwidget = QWidget(fuzzy_assigner_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setTabPosition(QTabWidget.North)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout = QGridLayout(self.tab_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphicsView = QGraphicsView(self.tab_1)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.label = QLabel(self.tab_1)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/newPrefix/contract_price_plot.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.tab_widget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_widget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tab_widget, 1, 0, 1, 1)

        self.variable_explain_lab = QLabel(self.centralwidget)
        self.variable_explain_lab.setObjectName(u"variable_explain_lab")
        font = QFont()
        font.setPointSize(16)
        self.variable_explain_lab.setFont(font)

        self.gridLayout_2.addWidget(self.variable_explain_lab, 0, 0, 1, 1)

        fuzzy_assigner_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(fuzzy_assigner_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1030, 21))
        self.menuLoad = QMenu(self.menubar)
        self.menuLoad.setObjectName(u"menuLoad")
        fuzzy_assigner_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(fuzzy_assigner_window)
        self.statusbar.setObjectName(u"statusbar")
        fuzzy_assigner_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLoad.menuAction())
        self.menuLoad.addAction(self.actionLoad)
        self.menuLoad.addAction(self.actionSave)

        self.retranslateUi(fuzzy_assigner_window)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(fuzzy_assigner_window)
    # setupUi

    def retranslateUi(self, fuzzy_assigner_window):
        fuzzy_assigner_window.setWindowTitle(QCoreApplication.translate("fuzzy_assigner_window", u"MainWindow", None))
        self.actionLoad.setText(QCoreApplication.translate("fuzzy_assigner_window", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("fuzzy_assigner_window", u"Save", None))
        self.label.setText("")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_1), QCoreApplication.translate("fuzzy_assigner_window", u"Tab 1", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), QCoreApplication.translate("fuzzy_assigner_window", u"Tab 2", None))
        self.variable_explain_lab.setText(QCoreApplication.translate("fuzzy_assigner_window", u"Price contract --- mm", None))
        self.menuLoad.setTitle(QCoreApplication.translate("fuzzy_assigner_window", u"File", None))
    # retranslateUi

