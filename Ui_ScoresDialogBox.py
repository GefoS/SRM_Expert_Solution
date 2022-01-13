from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_scores_dialog_box(object):
    def __init__(self):
        self.bad_score_style = "color: rgb(230, 0, 0);"
        self.medium_score_style = "color: rgb(255, 140, 0);"
        self.good_score_style = "color: rgb(34, 139, 34);"


    def setupUi(self, scores_dialog_box):
        if not scores_dialog_box.objectName():
            scores_dialog_box.setObjectName(u"scores_dialog_box")
        scores_dialog_box.resize(697, 666)
        scores_dialog_box.setMaximumSize(QSize(1000, 16777215))
        self.scores_dialog_box_widget = QWidget(scores_dialog_box)
        self.scores_dialog_box_widget.setObjectName(u"scores_dialog_box_widget")
        self.verticalLayout = QVBoxLayout(self.scores_dialog_box_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.label = QLabel(self.scores_dialog_box_widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)

        self.lb_total_score = QLabel(self.scores_dialog_box_widget)
        self.lb_total_score.setObjectName(u"lb_total_score")
        self.lb_total_score.setMinimumSize(QSize(85, 0))
        self.lb_total_score.setMaximumSize(QSize(85, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(27, 230, 13, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lb_total_score.setPalette(palette)
        self.lb_total_score.setFont(font)

        self.gridLayout.addWidget(self.lb_total_score, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(138, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(138, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.scores_dialog_box_widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.lb_contract_risk = QLabel(self.scores_dialog_box_widget)
        self.lb_contract_risk.setObjectName(u"lb_contract_risk")
        self.lb_contract_risk.setMinimumSize(QSize(85, 0))
        self.lb_contract_risk.setMaximumSize(QSize(150, 16777215))
        palette1 = QPalette()
        brush2 = QBrush(QColor(195, 13, 46, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lb_contract_risk.setPalette(palette1)
        self.lb_contract_risk.setFont(font)

        self.gridLayout.addWidget(self.lb_contract_risk, 1, 2, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(138, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.line_7 = QFrame(self.scores_dialog_box_widget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setLineWidth(1)
        self.line_7.setMidLineWidth(2)
        self.line_7.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.scores_dialog_box_widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(18)
        self.label_3.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lb_Supplying = QLabel(self.scores_dialog_box_widget)
        self.lb_Supplying.setObjectName(u"lb_Supplying")
        self.lb_Supplying.setMinimumSize(QSize(70, 0))
        self.lb_Supplying.setMaximumSize(QSize(70, 16777215))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lb_Supplying.setPalette(palette2)
        self.lb_Supplying.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lb_Supplying)


        self.horizontalLayout.addLayout(self.formLayout)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lb_supplying_result = QLabel(self.scores_dialog_box_widget)
        self.lb_supplying_result.setObjectName(u"lb_supplying_result")
        font2 = QFont()
        font2.setPointSize(12)
        self.lb_supplying_result.setFont(font2)
        self.lb_supplying_result.setWordWrap(True)

        self.verticalLayout.addWidget(self.lb_supplying_result)

        self.line_2 = QFrame(self.scores_dialog_box_widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.scores_dialog_box_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.lb_Legal_and_Compliance = QLabel(self.scores_dialog_box_widget)
        self.lb_Legal_and_Compliance.setObjectName(u"lb_Legal_and_Compliance")
        self.lb_Legal_and_Compliance.setMinimumSize(QSize(70, 0))
        self.lb_Legal_and_Compliance.setMaximumSize(QSize(70, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lb_Legal_and_Compliance.setPalette(palette3)
        self.lb_Legal_and_Compliance.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lb_Legal_and_Compliance)


        self.horizontalLayout_2.addLayout(self.formLayout_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lb_compliance_result = QLabel(self.scores_dialog_box_widget)
        self.lb_compliance_result.setObjectName(u"lb_compliance_result")
        self.lb_compliance_result.setFont(font2)
        self.lb_compliance_result.setWordWrap(True)

        self.verticalLayout.addWidget(self.lb_compliance_result)

        self.line_3 = QFrame(self.scores_dialog_box_widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_7 = QLabel(self.scores_dialog_box_widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.lb_Quality_as_BP = QLabel(self.scores_dialog_box_widget)
        self.lb_Quality_as_BP.setObjectName(u"lb_Quality_as_BP")
        self.lb_Quality_as_BP.setMinimumSize(QSize(70, 0))
        self.lb_Quality_as_BP.setMaximumSize(QSize(70, 16777215))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lb_Quality_as_BP.setPalette(palette4)
        self.lb_Quality_as_BP.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lb_Quality_as_BP)


        self.horizontalLayout_3.addLayout(self.formLayout_3)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.lb_quality_bp_result = QLabel(self.scores_dialog_box_widget)
        self.lb_quality_bp_result.setObjectName(u"lb_quality_bp_result")
        self.lb_quality_bp_result.setFont(font2)
        self.lb_quality_bp_result.setWordWrap(True)

        self.verticalLayout.addWidget(self.lb_quality_bp_result)

        self.line_5 = QFrame(self.scores_dialog_box_widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_9 = QLabel(self.scores_dialog_box_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.lb_Communications = QLabel(self.scores_dialog_box_widget)
        self.lb_Communications.setObjectName(u"lb_Communications")
        self.lb_Communications.setMinimumSize(QSize(70, 0))
        self.lb_Communications.setMaximumSize(QSize(70, 16777215))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lb_Communications.setPalette(palette5)
        self.lb_Communications.setFont(font1)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lb_Communications)


        self.horizontalLayout_4.addLayout(self.formLayout_4)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.lb_communications_result = QLabel(self.scores_dialog_box_widget)
        self.lb_communications_result.setObjectName(u"lb_communications_result")
        self.lb_communications_result.setFont(font2)
        self.lb_communications_result.setWordWrap(True)

        self.verticalLayout.addWidget(self.lb_communications_result)

        self.line_4 = QFrame(self.scores_dialog_box_widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_13)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_11 = QLabel(self.scores_dialog_box_widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.lb_EHS = QLabel(self.scores_dialog_box_widget)
        self.lb_EHS.setObjectName(u"lb_EHS")
        self.lb_EHS.setMinimumSize(QSize(70, 0))
        self.lb_EHS.setMaximumSize(QSize(70, 16777215))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.lb_EHS.setPalette(palette6)
        self.lb_EHS.setFont(font1)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.lb_EHS)


        self.horizontalLayout_5.addLayout(self.formLayout_5)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.lb_ehs_result = QLabel(self.scores_dialog_box_widget)
        self.lb_ehs_result.setObjectName(u"lb_ehs_result")
        self.lb_ehs_result.setFont(font2)
        self.lb_ehs_result.setWordWrap(True)

        self.verticalLayout.addWidget(self.lb_ehs_result)

        self.line_6 = QFrame(self.scores_dialog_box_widget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(1)
        self.line_6.setMidLineWidth(2)
        self.line_6.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line_6)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lb_final_result = QLabel(self.scores_dialog_box_widget)
        self.lb_final_result.setObjectName(u"lb_final_result")
        font3 = QFont()
        font3.setPointSize(22)
        self.lb_final_result.setFont(font3)
        self.lb_final_result.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_final_result)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        scores_dialog_box.setCentralWidget(self.scores_dialog_box_widget)

        self.retranslateUi(scores_dialog_box)

        QMetaObject.connectSlotsByName(scores_dialog_box)
    # setupUi

    def retranslateUi(self, scores_dialog_box):
        scores_dialog_box.setWindowTitle(QCoreApplication.translate("scores_dialog_box", u"Supplier scoring result", None))
        self.label.setText(QCoreApplication.translate("scores_dialog_box", u"Total supplier score:", None))
        self.lb_total_score.setText(QCoreApplication.translate("scores_dialog_box", u"10.00", None))
        self.label_2.setText(QCoreApplication.translate("scores_dialog_box", u"Contract risk:", None))
        self.lb_contract_risk.setText(QCoreApplication.translate("scores_dialog_box", u"Very risky", None))
        self.label_3.setText(QCoreApplication.translate("scores_dialog_box", u"Supplying score:", None))
        self.lb_Supplying.setText(QCoreApplication.translate("scores_dialog_box", u"10.00", None))
        self.lb_supplying_result.setText(QCoreApplication.translate("scores_dialog_box", u"TRALALLALALALALLALA  TRALALLALALALALLALA  TRALALLALALALALLALA TRALALLALALALALLALA  TRALALLALALALALLALA  TRALALLALALALALLALA ", None))
        self.label_5.setText(QCoreApplication.translate("scores_dialog_box", u"Legal and compliance score: ", None))
        self.lb_Legal_and_Compliance.setText(QCoreApplication.translate("scores_dialog_box", u"10.00", None))
        self.lb_compliance_result.setText(QCoreApplication.translate("scores_dialog_box", u"TRALALLALALALALLALA  TRALALLALALALALLALA  TRALALLALALALALLALA TRALALLALALALALLALA  TRALALLALALALALLALA  TRALALLALALALALLALA ", None))
        self.label_7.setText(QCoreApplication.translate("scores_dialog_box", u"Quality of the business partner:", None))
        self.lb_Quality_as_BP.setText(QCoreApplication.translate("scores_dialog_box", u"10.00", None))
        self.lb_quality_bp_result.setText(QCoreApplication.translate("scores_dialog_box", u"TRALALLALALALALLALA  TRALALLALALALALLALA  TRALALLALALALALLALA TRALALLALALALALLALA  TRALALLALALALALLALA  TRALALLALALALALLALA ", None))
        self.label_9.setText(QCoreApplication.translate("scores_dialog_box", u"Communications with the partner:", None))
        self.lb_Communications.setText(QCoreApplication.translate("scores_dialog_box", u"10.00", None))
        self.lb_communications_result.setText(QCoreApplication.translate("scores_dialog_box", u"TRALALLALALALALLALA  TRALALLALALALALLALA  TRALALLALALALALLALA TRALALLALALALALLALA  TRALALLALALALALLALA  TRALALLALALALALLALA ", None))
        self.label_11.setText(QCoreApplication.translate("scores_dialog_box", u"Environment, health and safety score:", None))
        self.lb_EHS.setText(QCoreApplication.translate("scores_dialog_box", u"10.00", None))
        self.lb_ehs_result.setText(QCoreApplication.translate("scores_dialog_box", u"TRALALLALALALALLALA  TRALALLALALALALLALA  TRALALLALALALALLALA TRALALLALALALALLALA  TRALALLALALALALLALA  TRALALLALALALALLALA ", None))
        self.lb_final_result.setText(QCoreApplication.translate("scores_dialog_box", u"Better to find new supplier", None))

        # retranslateUi

    def get_style_by_assessment(self, assessment):
        if assessment == "0":
            return self.bad_score_style
        elif assessment == "1":
            return self.medium_score_style
        else:
            return self.good_score_style

class ScoresWindow(QMainWindow):
    def __init__(self):
        super(ScoresWindow, self).__init__()

        self.ui = Ui_scores_dialog_box()
        self.ui.setupUi(self)

