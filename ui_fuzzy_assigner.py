# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitlednQhgMq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import util


class Ui_fuzzy_assigner_window(object):
    def setupUi(self, fuzzy_assigner_window):

        if not fuzzy_assigner_window.objectName():
            fuzzy_assigner_window.setObjectName(u"fuzzy_assigner_window")
        fuzzy_assigner_window.resize(1030, 642)

        self.actionLoad = QAction(fuzzy_assigner_window)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionSave = QAction(fuzzy_assigner_window)
        self.actionSave.setObjectName(u"actionSave")

        self.centralwidget = QWidget(fuzzy_assigner_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.fuzzy_variables_tabs = []
        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName(u"tab_widget")

        self.create_tabs_for_tab_widget(self.tab_widget)
        print(self.fuzzy_variables_tabs)

        self.gridLayout_2.addWidget(self.tab_widget, 0, 0, 1, 1)

        fuzzy_assigner_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(fuzzy_assigner_window)
        self.statusbar.setObjectName(u"statusbar")
        fuzzy_assigner_window.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(fuzzy_assigner_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1030, 21))
        self.menuLoad = QMenu(self.menubar)
        self.menuLoad.setObjectName(u"menuLoad")
        fuzzy_assigner_window.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuLoad.menuAction())
        self.menuLoad.addAction(self.actionLoad)
        self.menuLoad.addAction(self.actionSave)

        self.retranslateUi(fuzzy_assigner_window)
        self.actionLoad.triggered.connect(lambda : self.tab_widget.setTabText(self.tab_widget.indexOf(self.fuzzy_variables_tabs[3]), 'LOH'))

        QMetaObject.connectSlotsByName(fuzzy_assigner_window)

    # setupUi

    def create_tabs_for_tab_widget(self, tab_widget):
        current_variables_settings = util.load_fuzzy_variables()

        for k, v in current_variables_settings.items():
            n_tab = QWidget()
            n_tab.setObjectName(v.get('internal_name'))
            n_grid = QGridLayout(n_tab)
            n_grid.setObjectName(v.get('internal_name') + 'Grid')
            tab_widget.addTab(n_tab, v.get('nice_name'))
            self.fuzzy_variables_tabs.append(n_tab)
        # self.tab_1 = QWidget()
        # self.tab_1.setObjectName(u"tab_1")
        # self.gridLayout = QGridLayout(self.tab_1)
        # self.gridLayout.setObjectName(u"gridLayout")
        # self.tab_widget.addTab(self.tab_1, "")
        # self.tab_2 = QWidget()
        # self.tab_2.setObjectName(u"tab_2")
        # self.tab_widget.addTab(self.tab_2, "")

    def retranslateUi(self, fuzzy_assigner_window):
        fuzzy_assigner_window.setWindowTitle(QCoreApplication.translate("fuzzy_assigner_window", u"MainWindow", None))
        self.actionLoad.setText(QCoreApplication.translate("fuzzy_assigner_window", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("fuzzy_assigner_window", u"Save", None))
        # self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_1), QCoreApplication.translate("fuzzy_assigner_window", u"Tab 1", None))
        # self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), QCoreApplication.translate("fuzzy_assigner_window", u"Tab 2", None))
        self.menuLoad.setTitle(QCoreApplication.translate("fuzzy_assigner_window", u"File", None))
    # retranslateUi
