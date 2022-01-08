from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from os import path
import csv

import globals
import util

class Ui_fuzzy_assigner_window(object):
    def __init__(self):
        self.fuzzy_variables_tabs = []
        self.tabs_grids = []
        self.fuzzy_variables_tables = []
        self.membership_func_plots = []
        self.table_meta = []

        self.variables_measures = load_measures_settings()
        have_unsaved_changes = False

    def setupUi(self, fuzzy_assigner_window):

        if not fuzzy_assigner_window.objectName():
            fuzzy_assigner_window.setObjectName(u"fuzzy_assigner_window")
        fuzzy_assigner_window.resize(1024, 750)

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

        # self.create_tabs_for_tab_widget(self.tab_widget)
        self.load_variables_settings(self.tab_widget)

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

        self.menubar.addAction(self.menuLoad.menuAction())
        self.menuLoad.addAction(self.actionLoad)
        self.menuLoad.addAction(self.actionSave)

        self.retranslateUi(fuzzy_assigner_window)
        self.actionSave.triggered.connect(self.save_variables_settings)
        self.tab_widget.currentChanged.connect(self.change_measurement_label_text)

        for table in self.fuzzy_variables_tables:
            table.cellChanged.connect(self.repaint_current_plot)

        self.change_measurement_label_text()

        QMetaObject.connectSlotsByName(fuzzy_assigner_window)

    # setupUi

    def repaint_current_plot(self):
        tab_id = self.tab_widget.currentIndex()
        label, img_path = self.membership_func_plots[tab_id]
        table = self.fuzzy_variables_tables[tab_id]
        fuz_type = self.table_meta[tab_id][2]
        values = get_values_from_table(table, fuz_type)
        util.plot_membership_function (values, fuz_type,self.table_meta[tab_id][1], self.table_meta[tab_id][0])
        set_resized_pixmap(label, img_path)

    def save_variables_settings(self):
        current_variables_settings = util.load_fuzzy_variables()
        new_variables = []

        for table in self.fuzzy_variables_tables:
            var_name = table.objectName().replace('Table', '')
            var_settings = current_variables_settings.get(var_name)
            new_values = get_values_from_table(table, var_settings.get('fuzzy_type'))

            var_settings['universe_of_discourse'] = [float(table.item(table.rowCount() - 1, 0).text()),
                                                     float(table.item(table.rowCount() - 1, 1).text())]
            var_settings['values'] = new_values.copy()
            new_variables.append(var_settings)

        util.save_fuzzy_variables(new_variables, True)

    def load_variables_settings(self, tab_widget):
        current_variables_settings = util.load_fuzzy_variables()

        for k, v in current_variables_settings.items():
            n_tab = QWidget()
            n_tab.setObjectName(v.get('internal_name'))
            n_grid = QGridLayout(n_tab)
            n_grid.setObjectName(v.get('internal_name') + 'Grid')
            tab_widget.addTab(n_tab, v.get('nice_name'))
            n_table = QTableWidget(n_tab)
            n_table.setObjectName(v.get('internal_name') + 'Table')
            if n_table.columnCount() < 4:
                n_table.setColumnCount(4)
            for c in range(4):
                n_table.setHorizontalHeaderItem(c, QTableWidgetItem())
                n_table.horizontalHeaderItem(c).setText(globals.TABLE_COLUMN_NAMES[c]);

            variables_count = len(v.get('values').values())
            if n_table.rowCount() < variables_count:
                n_table.setRowCount(variables_count + 1)
            row_c = 0
            for ling_k, ling_v in v.get('values').items():
                n_table.setVerticalHeaderItem(row_c, QTableWidgetItem())
                n_table.verticalHeaderItem(row_c).setText(ling_k);
                for val in range(len(ling_v)):
                    n_table.setItem(row_c, val, QTableWidgetItem())
                    n_table.item(row_c, val).setText(str(ling_v[val]))
                row_c += 1

            n_table.setVerticalHeaderItem(variables_count, QTableWidgetItem())
            n_table.verticalHeaderItem(variables_count).setText('Universe of discourse')
            univ_of_disc = v.get('universe_of_discourse')
            for uc in range(2):
                n_table.setItem(variables_count, uc, QTableWidgetItem())
                n_table.item(variables_count, uc).setText(str(univ_of_disc[uc]))

            n_grid.addWidget(n_table, 0, 0, 1, 1)

            if not path.exists(util.get_plot_img_name(v.get('internal_name'))):
                util.plot_membership_function(v.get('values'),
                                              v.get('fuzzy_type'),
                                              v.get('nice_name'),
                                              v.get('internal_name'))

            plot_lab = QLabel(n_tab)
            plot_lab.setMaximumHeight(350)
            plot_lab.setObjectName(v.get('internal_name') + '_plot_lab')
            set_resized_pixmap(plot_lab, util.get_plot_img_name(v.get('internal_name')))
            plot_lab.setAlignment(Qt.AlignCenter)
            n_grid.addWidget(plot_lab, 1, 0, 1, 1)
            # plot_lab.re


            self.membership_func_plots.append((plot_lab, util.get_plot_img_name(v.get('internal_name'))))
            self.table_meta.append((
                v.get('internal_name'),
                v.get('nice_name'),
                v.get('fuzzy_type')
            ))
            self.tabs_grids.append(n_grid)
            self.fuzzy_variables_tabs.append(n_tab)
            self.fuzzy_variables_tables.append(n_table)

    def retranslateUi(self, fuzzy_assigner_window):
        fuzzy_assigner_window.setWindowTitle(QCoreApplication.translate("fuzzy_assigner_window", u"MainWindow", None))
        self.actionLoad.setText(QCoreApplication.translate("fuzzy_assigner_window", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("fuzzy_assigner_window", u"Save", None))
        # self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_1), QCoreApplication.translate("fuzzy_assigner_window", u"Tab 1", None))
        # self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), QCoreApplication.translate("fuzzy_assigner_window", u"Tab 2", None))
        self.menuLoad.setTitle(QCoreApplication.translate("fuzzy_assigner_window", u"File", None))

    # retranslateUi

    def change_measurement_label_text(self):
        nice_name, measure = self.variables_measures.get(
            self.fuzzy_variables_tabs[self.tab_widget.currentIndex()].objectName()
        )
        i = 0

        self.variable_explain_lab.setText(nice_name+' - '+measure)


def get_values_from_table(table, fuz_type):
    new_values = {}
    column_range = range(1)
    if fuz_type == 'fuzzy':
        column_range = range(table.columnCount())
    else:
        column_range = range(2)
    for r in range(table.rowCount() - 1):
        val_name = table.verticalHeaderItem(r).text()
        new_values[val_name] = [float(table.item(r, c).text()) for c in column_range]
    return new_values


def set_resized_pixmap(label, img_path):
    pix = QPixmap(img_path)
    label.setPixmap(pix.scaled(1024, 350, Qt.KeepAspectRatio, Qt.SmoothTransformation))


def load_measures_settings():
    measures = {}

    with open(globals.VARIABLES_MEASURES, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=globals.CSV_DELIMITER)
        for row in list(reader)[1:]:
            measures[row[0]] = (row[1], row[2])
    return measures
