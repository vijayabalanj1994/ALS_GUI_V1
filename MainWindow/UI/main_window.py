# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)
import gui_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(919, 802)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        font = QFont()
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_browse = QPushButton(self.groupBox_5)
        self.pb_browse.setObjectName(u"pb_browse")

        self.gridLayout.addWidget(self.pb_browse, 0, 0, 1, 1)

        self.pb_run = QPushButton(self.groupBox_5)
        self.pb_run.setObjectName(u"pb_run")

        self.gridLayout.addWidget(self.pb_run, 0, 1, 1, 1)

        self.pb_export_results = QPushButton(self.groupBox_5)
        self.pb_export_results.setObjectName(u"pb_export_results")

        self.gridLayout.addWidget(self.pb_export_results, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox_5, 2, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(425, 425))
        self.groupBox_4.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_CAM_image = QLabel(self.groupBox_4)
        self.lb_CAM_image.setObjectName(u"lb_CAM_image")
        self.lb_CAM_image.setMinimumSize(QSize(400, 400))
        self.lb_CAM_image.setMaximumSize(QSize(400, 400))
        self.lb_CAM_image.setFont(font)
        self.lb_CAM_image.setFrameShape(QFrame.WinPanel)
        self.lb_CAM_image.setPixmap(QPixmap(u":/main/NeroBioMark_Logo.png"))
        self.lb_CAM_image.setScaledContents(True)
        self.lb_CAM_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_CAM_image)


        self.gridLayout_4.addWidget(self.groupBox_4, 1, 3, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(425, 425))
        self.groupBox_2.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_input_image = QLabel(self.groupBox_2)
        self.lb_input_image.setObjectName(u"lb_input_image")
        self.lb_input_image.setMinimumSize(QSize(400, 400))
        self.lb_input_image.setMaximumSize(QSize(400, 400))
        self.lb_input_image.setFont(font)
        self.lb_input_image.setFrameShape(QFrame.WinPanel)
        self.lb_input_image.setPixmap(QPixmap(u":/main/NeroBioMark_Logo.png"))
        self.lb_input_image.setScaledContents(True)
        self.lb_input_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_input_image)


        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font)
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.p_bar_control = QProgressBar(self.groupBox_3)
        self.p_bar_control.setObjectName(u"p_bar_control")
        self.p_bar_control.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #4CAF50; /* green */\n"
"    width: 10px;\n"
"}")
        self.p_bar_control.setValue(0)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.p_bar_control)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.p_bar_discordant = QProgressBar(self.groupBox_3)
        self.p_bar_discordant.setObjectName(u"p_bar_discordant")
        self.p_bar_discordant.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #FFA726;\n"
"    width: 10px;\n"
"}")
        self.p_bar_discordant.setValue(0)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.p_bar_discordant)

        self.p_bar_concordant = QProgressBar(self.groupBox_3)
        self.p_bar_concordant.setObjectName(u"p_bar_concordant")
        self.p_bar_concordant.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #EF6C00;\n"
"    width: 10px;\n"
"}\n"
"")
        self.p_bar_concordant.setValue(0)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.p_bar_concordant)


        self.gridLayout_4.addWidget(self.groupBox_3, 2, 3, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 100))
        self.label.setMaximumSize(QSize(100, 100))
        self.label.setPixmap(QPixmap(u":/main/NeroBioMark_Logo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(700, 100))
        font1 = QFont()
        font1.setPointSize(40)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 1, 2, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 919, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pb_browse.setText(QCoreApplication.translate("MainWindow", u"Browse ", None))
        self.pb_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.pb_export_results.setText(QCoreApplication.translate("MainWindow", u"Export Results", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"CAM Image", None))
        self.lb_CAM_image.setText(QCoreApplication.translate("MainWindow", u"Run Model", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.lb_input_image.setText(QCoreApplication.translate("MainWindow", u"Browse Image", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Discordant", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Concordant", None))
        self.groupBox.setTitle("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ALS Diagnostic Assistant", None))
    # retranslateUi

