import json

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import global_params
import util
from fuzzy_module import FuzzyModule

from Ui_ScoresDialogBox import ScoresWindow


class Ui_SRM_Expert_Main_Window(object):

    def __init__(self):
        self.fuzzy_module_main = FuzzyModule()

    def init_object_lists(self):

        self.scores_dialog = ScoresWindow()

        with open(global_params.SCORE_ASSESSMENTS_FILE, "r") as json_file:
            self.score_assessment = json.loads(json_file.read())

        self.sliders = [
            self.sld_overall_quality,
            self.sld_information_share,
            self.sld_overall_communications,
            self.sld_financial_sustainability,
            self.sld_environment_safety,
            self.sld_work_safety
        ]

        self.fields_for_sliders = [
            self.le_overall_quality,
            self.le_information_share,
            self.le_overall_communications,
            self.le_financial_sustainability,
            self.le_environment_safety,
            self.le_work_safety
        ]

    def setupUi(self, SRM_Expert_Main_Window):
        if not SRM_Expert_Main_Window.objectName():
            SRM_Expert_Main_Window.setObjectName(u"SRM_Expert_Main_Window")
        SRM_Expert_Main_Window.resize(407, 793)
        self.centralwidget = QWidget(SRM_Expert_Main_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QSize(100, 32))
        self.label_21.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setPointSize(16)
        self.label_21.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_21)

        self.le_supplier_name = QLineEdit(self.centralwidget)
        self.le_supplier_name.setObjectName(u"le_supplier_name")
        self.le_supplier_name.setMinimumSize(QSize(200, 32))
        self.le_supplier_name.setMaximumSize(QSize(400, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        self.le_supplier_name.setFont(font1)

        self.horizontalLayout_7.addWidget(self.le_supplier_name)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(100, 0))
        self.label_22.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_22.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_22)

        self.le_tax_id = QLineEdit(self.centralwidget)
        self.le_tax_id.setObjectName(u"le_tax_id")
        self.le_tax_id.setMinimumSize(QSize(200, 0))
        self.le_tax_id.setMaximumSize(QSize(400, 16777215))
        self.le_tax_id.setFont(font2)

        self.horizontalLayout_8.addWidget(self.le_tax_id)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(100, 0))
        self.label_23.setMaximumSize(QSize(100, 16777215))
        font3 = QFont()
        font3.setPointSize(9)
        self.label_23.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_23)

        self.le_reg_id = QLineEdit(self.centralwidget)
        self.le_reg_id.setObjectName(u"le_reg_id")
        self.le_reg_id.setMinimumSize(QSize(200, 0))
        self.le_reg_id.setMaximumSize(QSize(400, 16777215))
        self.le_reg_id.setFont(font2)

        self.horizontalLayout_9.addWidget(self.le_reg_id)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.gridLayout_2.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(160, 0))
        self.label.setFont(font2)

        self.horizontalLayout.addWidget(self.label)

        self.le_contract_price = QLineEdit(self.centralwidget)
        self.le_contract_price.setObjectName(u"le_contract_price")
        self.le_contract_price.setMinimumSize(QSize(80, 0))
        self.le_contract_price.setMaximumSize(QSize(80, 16777215))
        font4 = QFont()
        font4.setPointSize(10)
        self.le_contract_price.setFont(font4)

        self.horizontalLayout.addWidget(self.le_contract_price)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(60, 0))
        self.label_16.setFont(font4)

        self.horizontalLayout.addWidget(self.label_16)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(160, 0))
        self.label_2.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radio_type_one_time = QRadioButton(self.centralwidget)
        self.radio_type_one_time.setObjectName(u"radio_type_one_time")
        self.radio_type_one_time.setFont(font4)
        self.radio_type_one_time.setChecked(True)

        self.verticalLayout.addWidget(self.radio_type_one_time)

        self.radio_type_long = QRadioButton(self.centralwidget)
        self.radio_type_long.setObjectName(u"radio_type_long")
        self.radio_type_long.setFont(font4)

        self.verticalLayout.addWidget(self.radio_type_long)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(160, 0))
        self.label_3.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.le_experience = QLineEdit(self.centralwidget)
        self.le_experience.setObjectName(u"le_experience")
        self.le_experience.setMinimumSize(QSize(80, 0))
        self.le_experience.setMaximumSize(QSize(80, 16777215))
        self.le_experience.setFont(font4)

        self.horizontalLayout_2.addWidget(self.le_experience)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(60, 0))
        self.label_15.setFont(font4)

        self.horizontalLayout_2.addWidget(self.label_15)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(160, 0))
        self.label_4.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.sld_overall_quality = QSlider(self.centralwidget)
        self.sld_overall_quality.setObjectName(u"sld_overall_quality")
        self.sld_overall_quality.setMinimumSize(QSize(180, 0))
        self.sld_overall_quality.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.sld_overall_quality)

        self.le_overall_quality = QLineEdit(self.centralwidget)
        self.le_overall_quality.setObjectName(u"le_overall_quality")
        self.le_overall_quality.setMinimumSize(QSize(35, 0))
        self.le_overall_quality.setMaximumSize(QSize(35, 16777215))
        self.le_overall_quality.setFont(font4)

        self.horizontalLayout_4.addWidget(self.le_overall_quality)

        self.gridLayout_2.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(160, 0))
        self.label_18.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_18)

        self.le_delayed_deliveries = QLineEdit(self.centralwidget)
        self.le_delayed_deliveries.setObjectName(u"le_delayed_deliveries")
        self.le_delayed_deliveries.setMinimumSize(QSize(40, 0))
        self.le_delayed_deliveries.setMaximumSize(QSize(80, 16777215))
        self.le_delayed_deliveries.setFont(font4)

        self.horizontalLayout_5.addWidget(self.le_delayed_deliveries)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(60, 0))
        self.label_17.setFont(font4)

        self.horizontalLayout_5.addWidget(self.label_17)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.gridLayout_2.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(160, 0))
        self.label_19.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_19)

        self.le_average_delay_delivery = QLineEdit(self.centralwidget)
        self.le_average_delay_delivery.setObjectName(u"le_average_delay_delivery")
        self.le_average_delay_delivery.setMinimumSize(QSize(40, 0))
        self.le_average_delay_delivery.setMaximumSize(QSize(80, 16777215))
        self.le_average_delay_delivery.setFont(font4)

        self.horizontalLayout_6.addWidget(self.le_average_delay_delivery)

        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(60, 0))
        self.label_20.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label_20)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.gridLayout_2.addLayout(self.horizontalLayout_6, 6, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(160, 0))
        self.label_5.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_5)

        self.sld_information_share = QSlider(self.centralwidget)
        self.sld_information_share.setObjectName(u"sld_information_share")
        self.sld_information_share.setMinimumSize(QSize(180, 0))
        self.sld_information_share.setOrientation(Qt.Horizontal)

        self.horizontalLayout_11.addWidget(self.sld_information_share)

        self.le_information_share = QLineEdit(self.centralwidget)
        self.le_information_share.setObjectName(u"le_information_share")
        self.le_information_share.setMinimumSize(QSize(35, 0))
        self.le_information_share.setMaximumSize(QSize(35, 16777215))
        self.le_information_share.setFont(font4)

        self.horizontalLayout_11.addWidget(self.le_information_share)

        self.gridLayout_2.addLayout(self.horizontalLayout_11, 7, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(160, 0))
        self.label_6.setFont(font2)
        self.label_6.setWordWrap(True)

        self.horizontalLayout_12.addWidget(self.label_6)

        self.sld_overall_communications = QSlider(self.centralwidget)
        self.sld_overall_communications.setObjectName(u"sld_overall_communications")
        self.sld_overall_communications.setMinimumSize(QSize(180, 0))
        self.sld_overall_communications.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.sld_overall_communications)

        self.le_overall_communications = QLineEdit(self.centralwidget)
        self.le_overall_communications.setObjectName(u"le_overall_communications")
        self.le_overall_communications.setMinimumSize(QSize(22, 0))
        self.le_overall_communications.setMaximumSize(QSize(100, 16777215))
        self.le_overall_communications.setFont(font4)

        self.horizontalLayout_12.addWidget(self.le_overall_communications)

        self.gridLayout_2.addLayout(self.horizontalLayout_12, 8, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(160, 0))
        self.label_7.setFont(font2)

        self.horizontalLayout_13.addWidget(self.label_7)

        self.sld_financial_sustainability = QSlider(self.centralwidget)
        self.sld_financial_sustainability.setObjectName(u"sld_financial_sustainability")
        self.sld_financial_sustainability.setMinimumSize(QSize(180, 0))
        self.sld_financial_sustainability.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.sld_financial_sustainability)

        self.le_financial_sustainability = QLineEdit(self.centralwidget)
        self.le_financial_sustainability.setObjectName(u"le_financial_sustainability")
        self.le_financial_sustainability.setMinimumSize(QSize(35, 0))
        self.le_financial_sustainability.setMaximumSize(QSize(35, 16777215))
        self.le_financial_sustainability.setFont(font4)

        self.horizontalLayout_13.addWidget(self.le_financial_sustainability)

        self.gridLayout_2.addLayout(self.horizontalLayout_13, 9, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(160, 0))
        self.label_24.setFont(font2)

        self.horizontalLayout_14.addWidget(self.label_24)

        self.le_overall_compliance = QLineEdit(self.centralwidget)
        self.le_overall_compliance.setObjectName(u"le_overall_compliance")
        self.le_overall_compliance.setMinimumSize(QSize(40, 0))
        self.le_overall_compliance.setMaximumSize(QSize(80, 16777215))
        self.le_overall_compliance.setFont(font4)

        self.horizontalLayout_14.addWidget(self.le_overall_compliance)

        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(60, 0))
        self.label_25.setFont(font4)

        self.horizontalLayout_14.addWidget(self.label_25)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.gridLayout_2.addLayout(self.horizontalLayout_14, 10, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.cb_has_necessary_certification = QCheckBox(self.centralwidget)
        self.cb_has_necessary_certification.setObjectName(u"cb_has_necessary_certification")
        self.cb_has_necessary_certification.setMinimumSize(QSize(200, 0))
        self.cb_has_necessary_certification.setFont(font2)

        self.horizontalLayout_15.addWidget(self.cb_has_necessary_certification)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_8)

        self.gridLayout_2.addLayout(self.horizontalLayout_15, 11, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(160, 0))
        self.label_29.setFont(font2)

        self.horizontalLayout_16.addWidget(self.label_29)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(100, 0))
        self.label_27.setMaximumSize(QSize(100, 16777215))
        self.label_27.setFont(font4)

        self.gridLayout.addWidget(self.label_27, 1, 2, 1, 1)

        self.le_court_partp_plaintiff_w = QLineEdit(self.centralwidget)
        self.le_court_partp_plaintiff_w.setObjectName(u"le_court_partp_plaintiff_w")
        self.le_court_partp_plaintiff_w.setMinimumSize(QSize(35, 0))
        self.le_court_partp_plaintiff_w.setMaximumSize(QSize(35, 16777215))
        self.le_court_partp_plaintiff_w.setFont(font4)

        self.gridLayout.addWidget(self.le_court_partp_plaintiff_w, 1, 0, 1, 1)

        self.le_court_partp_defendant_w = QLineEdit(self.centralwidget)
        self.le_court_partp_defendant_w.setObjectName(u"le_court_partp_defendant_w")
        self.le_court_partp_defendant_w.setMinimumSize(QSize(35, 0))
        self.le_court_partp_defendant_w.setMaximumSize(QSize(35, 16777215))
        self.le_court_partp_defendant_w.setFont(font4)

        self.gridLayout.addWidget(self.le_court_partp_defendant_w, 2, 0, 1, 1)

        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(100, 0))
        self.label_26.setMaximumSize(QSize(100, 16777215))
        self.label_26.setFont(font4)

        self.gridLayout.addWidget(self.label_26, 3, 2, 1, 1)

        self.le_court_partp_plaintiff_l = QLineEdit(self.centralwidget)
        self.le_court_partp_plaintiff_l.setObjectName(u"le_court_partp_plaintiff_l")
        self.le_court_partp_plaintiff_l.setMinimumSize(QSize(35, 0))
        self.le_court_partp_plaintiff_l.setMaximumSize(QSize(35, 16777215))
        self.le_court_partp_plaintiff_l.setFont(font4)

        self.gridLayout.addWidget(self.le_court_partp_plaintiff_l, 1, 1, 1, 1)

        self.le_court_partp_defendant_l = QLineEdit(self.centralwidget)
        self.le_court_partp_defendant_l.setObjectName(u"le_court_partp_defendant_l")
        self.le_court_partp_defendant_l.setMinimumSize(QSize(35, 0))
        self.le_court_partp_defendant_l.setMaximumSize(QSize(35, 16777215))
        self.le_court_partp_defendant_l.setFont(font4)

        self.gridLayout.addWidget(self.le_court_partp_defendant_l, 2, 1, 1, 1)

        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(100, 0))
        self.label_28.setMaximumSize(QSize(100, 16777215))
        self.label_28.setFont(font4)

        self.gridLayout.addWidget(self.label_28, 2, 2, 1, 1)

        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(35, 0))
        self.label_31.setMaximumSize(QSize(35, 16777215))
        self.label_31.setFont(font4)

        self.gridLayout.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(35, 0))
        self.label_30.setMaximumSize(QSize(35, 16777215))
        self.label_30.setFont(font4)

        self.gridLayout.addWidget(self.label_30, 0, 1, 1, 1)

        self.le_court_partp_third_side = QLineEdit(self.centralwidget)
        self.le_court_partp_third_side.setObjectName(u"le_court_partp_third_side")
        self.le_court_partp_third_side.setMinimumSize(QSize(35, 0))
        self.le_court_partp_third_side.setMaximumSize(QSize(75, 16777215))
        self.le_court_partp_third_side.setFont(font4)

        self.gridLayout.addWidget(self.le_court_partp_third_side, 3, 0, 1, 2)

        self.horizontalLayout_16.addLayout(self.gridLayout)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_9)

        self.gridLayout_2.addLayout(self.horizontalLayout_16, 12, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(160, 0))
        self.label_8.setFont(font2)

        self.horizontalLayout_17.addWidget(self.label_8)

        self.sld_environment_safety = QSlider(self.centralwidget)
        self.sld_environment_safety.setObjectName(u"sld_environment_safety")
        self.sld_environment_safety.setMinimumSize(QSize(180, 0))
        self.sld_environment_safety.setOrientation(Qt.Horizontal)

        self.horizontalLayout_17.addWidget(self.sld_environment_safety)

        self.le_environment_safety = QLineEdit(self.centralwidget)
        self.le_environment_safety.setObjectName(u"le_environment_safety")
        self.le_environment_safety.setMinimumSize(QSize(35, 0))
        self.le_environment_safety.setMaximumSize(QSize(35, 16777215))
        self.le_environment_safety.setFont(font4)

        self.horizontalLayout_17.addWidget(self.le_environment_safety)

        self.gridLayout_2.addLayout(self.horizontalLayout_17, 13, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(160, 0))
        self.label_9.setFont(font2)

        self.horizontalLayout_18.addWidget(self.label_9)

        self.sld_work_safety = QSlider(self.centralwidget)
        self.sld_work_safety.setObjectName(u"sld_work_safety")
        self.sld_work_safety.setMinimumSize(QSize(180, 0))
        self.sld_work_safety.setOrientation(Qt.Horizontal)

        self.horizontalLayout_18.addWidget(self.sld_work_safety)

        self.le_work_safety = QLineEdit(self.centralwidget)
        self.le_work_safety.setObjectName(u"le_work_safety")
        self.le_work_safety.setMinimumSize(QSize(35, 0))
        self.le_work_safety.setMaximumSize(QSize(35, 16777215))
        self.le_work_safety.setFont(font4)

        self.horizontalLayout_18.addWidget(self.le_work_safety)

        self.gridLayout_2.addLayout(self.horizontalLayout_18, 14, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_10 = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_10)

        self.btn_calculate_score = QPushButton(self.centralwidget)
        self.btn_calculate_score.setObjectName(u"btn_calculate_score")
        self.btn_calculate_score.setMinimumSize(QSize(120, 40))
        self.btn_calculate_score.setFont(font2)

        self.horizontalLayout_19.addWidget(self.btn_calculate_score)

        self.gridLayout_2.addLayout(self.horizontalLayout_19, 15, 0, 1, 1)

        SRM_Expert_Main_Window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SRM_Expert_Main_Window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 407, 21))
        SRM_Expert_Main_Window.setMenuBar(self.menubar)

        self.retranslateUi(SRM_Expert_Main_Window)

        QMetaObject.connectSlotsByName(SRM_Expert_Main_Window)

        #END OF GENERATED CODE INSERTION POINT
        self.init_object_lists()
        self.init_connections()
    # setupUi

    def retranslateUi(self, SRM_Expert_Main_Window):
        SRM_Expert_Main_Window.setWindowTitle(QCoreApplication.translate("SRM_Expert_Main_Window", u"SRM Expert Solution", None))
        self.label_21.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Supplier", None))
        #self.le_supplier_name.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"ER-Telekom Holding", None))
        self.label_22.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Tax ID", None))
        #self.le_tax_id.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"5902202276", None))
        self.label_23.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Registration num", None))
        #self.le_reg_id.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"1065902028620", None))
        self.label.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Contract price", None))
        self.le_contract_price.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.label_16.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"USD", None))
        self.label_2.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Contract type", None))
        self.radio_type_one_time.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"One-time", None))
        self.radio_type_long.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Long", None))
        self.label_3.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Experience", None))
        #self.le_experience.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"150", None))
        self.label_15.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"years", None))
        self.label_4.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Overall quality", None))
        self.le_overall_quality.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.label_18.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Delayed deliveries", None))
        self.le_delayed_deliveries.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.label_17.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"%", None))
        self.label_19.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Average delay time", None))
        self.le_average_delay_delivery.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.label_20.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"hours", None))
        self.label_5.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Information share", None))
        self.le_information_share.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.label_6.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Communications with supplier", None))
        self.le_overall_communications.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.label_7.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Financial sustainability", None))
        self.le_financial_sustainability.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.label_24.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Overall compliance", None))
        #self.le_overall_compliance.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"100", None))
        self.label_25.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"%", None))
        self.cb_has_necessary_certification.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Has necessary certifications", None))
        self.label_29.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Participation in courts", None))
        self.label_27.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"As a plaintiff", None))
        self.le_court_partp_plaintiff_w.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.le_court_partp_defendant_w.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.label_26.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"As a third side", None))
        self.le_court_partp_plaintiff_l.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.le_court_partp_defendant_l.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.label_28.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"As a defendant", None))
        self.label_31.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Won", None))
        self.label_30.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Lost", None))
        self.le_court_partp_third_side.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.label_8.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Environment safety", None))
        self.le_environment_safety.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.label_9.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Work safety", None))
        self.le_work_safety.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"0", None))
        self.btn_calculate_score.setText(QCoreApplication.translate("SRM_Expert_Main_Window", u"Calculate score", None))
    # retranslateUi

    def calculate_final_score(self):
        current_results = util.load_saved_variables()
        contract_type = 1
        has_certs = 2
        if self.radio_type_one_time.isChecked():
            contract_type = 2
        if not self.cb_has_necessary_certification.isChecked():
           has_certs = 0
        new_results = {
            "contract_price": float(self.le_contract_price.text()),
            "contract_type": contract_type,
            "experience": float(self.le_experience.text()),
            "overall_quality": float(self.le_overall_quality.text()),
            "delayed_deliveries": float(self.le_delayed_deliveries.text()),
            "average_delay_delivery": float(self.le_average_delay_delivery.text()),
            "information_share": float(self.le_information_share.text()),
            "overall_communications": float(self.le_overall_communications.text()),
            "financial_sustainability": float(self.le_financial_sustainability.text()),
            "overall_compliance": float(self.le_overall_compliance.text()),
            "has_necessary_certification": has_certs,
            "court_history_defender_won": int(self.le_court_partp_defendant_w.text()),
            "court_history_plaintiff_won": int(self.le_court_partp_plaintiff_w.text()),
            "court_history_defender_lose": int(self.le_court_partp_defendant_l.text()),
            "court_history_plaintiff_lose": int(self.le_court_partp_plaintiff_l.text()),
            "court_history_third_side": int(self.le_court_partp_third_side.text()),
            "environment_safety": float(self.le_environment_safety.text()),
            "work_safety": float(self.le_work_safety.text())

        }
        current_results[self.le_supplier_name.text()] = new_results
        self.fuzzy_module_main.set_variables_val_in_module(new_results)
        scores, total_score = self.fuzzy_module_main.fire_main_fuzzy_system(0)
        print(scores, total_score)
        #total
        total_assessment = util.get_score_assessment(total_score)
        self.scores_dialog.ui.lb_total_score.setText(str(total_score))
        self.scores_dialog.ui.lb_final_result.setText(self.score_assessment.get(
            'Total').get(total_assessment))
        self.scores_dialog.ui.lb_total_score.setStyleSheet(
            self.scores_dialog.ui.get_style_by_assessment(total_assessment))

        if not self.scores_dialog.isVisible():
            self.scores_dialog.show()
        #self.scores_dialog.ui.lb_total_score.setText(str(res[1]))
        contract_risk = self.fuzzy_module_main.fire_contracting_fuzzy_system(new_results)
        if contract_risk == 3:
            self.scores_dialog.ui.lb_contract_risk.setText('Stable')
            self.scores_dialog.ui.lb_contract_risk.setStyleSheet(self.scores_dialog.ui.good_score_style)
        elif contract_risk == 2:
            self.scores_dialog.ui.lb_contract_risk.setText('Risky')
            self.scores_dialog.ui.lb_contract_risk.setStyleSheet(self.scores_dialog.ui.medium_score_style)
        else:
            self.scores_dialog.ui.lb_contract_risk.setText('Very risky')
            self.scores_dialog.ui.lb_contract_risk.setStyleSheet(self.scores_dialog.ui.bad_score_style)

        #supplying
        supply_score = float(scores.get('Supplying'))
        supply_assessment = util.get_score_assessment(supply_score)
        self.scores_dialog.ui.lb_Supplying.setText(str(supply_score))
        self.scores_dialog.ui.lb_supplying_result.setText(self.score_assessment.get(
            'Supplying').get(supply_assessment))
        self.scores_dialog.ui.lb_Supplying.setStyleSheet(self.scores_dialog.ui.get_style_by_assessment(supply_assessment))

        communications_score = float(scores.get('Communications'))
        communications_assessment = util.get_score_assessment(communications_score)
        self.scores_dialog.ui.lb_Communications.setText(str(communications_score))
        self.scores_dialog.ui.lb_communications_result.setText(self.score_assessment.get(
            'Communications').get(communications_assessment))
        self.scores_dialog.ui.lb_Communications.setStyleSheet(
            self.scores_dialog.ui.get_style_by_assessment(communications_assessment))

        legal_score = float(scores.get('Legal_and_Compliance'))
        legal_assessment = util.get_score_assessment(legal_score)
        self.scores_dialog.ui.lb_Legal_and_Compliance.setText(str(legal_score))
        self.scores_dialog.ui.lb_compliance_result.setText(self.score_assessment.get(
            'Legal_and_Compliance').get(legal_assessment))
        self.scores_dialog.ui.lb_Legal_and_Compliance.setStyleSheet(
            self.scores_dialog.ui.get_style_by_assessment(legal_assessment))

        EHS_score = float(scores.get('EHS'))
        EHS_assessment = util.get_score_assessment(EHS_score)
        self.scores_dialog.ui.lb_EHS.setText(str(EHS_score))
        self.scores_dialog.ui.lb_ehs_result.setText(self.score_assessment.get(
            'EHS').get(EHS_assessment))
        self.scores_dialog.ui.lb_EHS.setStyleSheet(
            self.scores_dialog.ui.get_style_by_assessment(EHS_assessment))

        Quality_as_BP_score = float(scores.get('Quality_as_BP'))
        Quality_as_BP_assessment = util.get_score_assessment(Quality_as_BP_score)
        self.scores_dialog.ui.lb_Quality_as_BP.setText(str(Quality_as_BP_score))
        self.scores_dialog.ui.lb_quality_bp_result.setText(self.score_assessment.get(
            'Supplying').get(Quality_as_BP_assessment))
        self.scores_dialog.ui.lb_Quality_as_BP.setStyleSheet(
            self.scores_dialog.ui.get_style_by_assessment(Quality_as_BP_assessment))


        with open(global_params.RESULT_SCORES_FILE, 'w') as json_file:
            json_file.write(json.dumps(current_results, indent=4))

    def init_connections(self):
        self.sld_overall_quality.sliderMoved.connect(lambda x:
                                                     self.le_overall_quality.setText(
                                                         str(float(x)/10)
                                                     ))
        self.sld_information_share.sliderMoved.connect(lambda x:
                                                     self.le_information_share.setText(
                                                         str(float(x)/10)
                                                     ))
        self.sld_overall_communications.sliderMoved.connect(lambda x:
                                                     self.le_overall_communications.setText(
                                                         str(float(x) / 10)
                                                     ))
        self.sld_financial_sustainability.sliderMoved.connect(lambda x:
                                                     self.le_financial_sustainability.setText(
                                                         str(float(x)/10)
                                                     ))
        self.sld_environment_safety.sliderMoved.connect(lambda x:
                                                     self.le_environment_safety.setText(
                                                         str(float(x) / 10)
                                                     ))
        self.sld_work_safety.sliderMoved.connect(lambda x:
                                                     self.le_work_safety.setText(
                                                         str(float(x) / 10)
                                                     ))

        self.btn_calculate_score.clicked.connect(self.calculate_final_score)
