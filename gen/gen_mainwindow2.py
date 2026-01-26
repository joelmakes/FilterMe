# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_FilterMe(object):
    def setupUi(self, FilterMe):
        if not FilterMe.objectName():
            FilterMe.setObjectName(u"FilterMe")
        FilterMe.resize(1084, 866)
        FilterMe.setMinimumSize(QSize(1084, 866))
        FilterMe.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        FilterMe.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"")
        FilterMe.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(FilterMe)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.webcam_Display = QLabel(self.centralwidget)
        self.webcam_Display.setObjectName(u"webcam_Display")

        self.verticalLayout.addWidget(self.webcam_Display)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_rio = QPushButton(self.centralwidget)
        self.pushButton_rio.setObjectName(u"pushButton_rio")

        self.horizontalLayout.addWidget(self.pushButton_rio)

        self.pushButton_sketch = QPushButton(self.centralwidget)
        self.pushButton_sketch.setObjectName(u"pushButton_sketch")

        self.horizontalLayout.addWidget(self.pushButton_sketch)

        self.pushButton_glasses = QPushButton(self.centralwidget)
        self.pushButton_glasses.setObjectName(u"pushButton_glasses")
        self.pushButton_glasses.setAutoDefault(False)
        self.pushButton_glasses.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_glasses)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_insert_username = QLineEdit(self.centralwidget)
        self.lineEdit_insert_username.setObjectName(u"lineEdit_insert_username")
        self.lineEdit_insert_username.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.lineEdit_insert_username, 0, Qt.AlignmentFlag.AlignVCenter)

        self.pushButton_take_photo_button = QPushButton(self.centralwidget)
        self.pushButton_take_photo_button.setObjectName(u"pushButton_take_photo_button")

        self.verticalLayout_2.addWidget(self.pushButton_take_photo_button)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        FilterMe.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FilterMe)
        self.statusbar.setObjectName(u"statusbar")
        FilterMe.setStatusBar(self.statusbar)

        self.retranslateUi(FilterMe)

        self.pushButton_glasses.setDefault(False)


        QMetaObject.connectSlotsByName(FilterMe)
    # setupUi

    def retranslateUi(self, FilterMe):
        FilterMe.setWindowTitle(QCoreApplication.translate("FilterMe", u"FilterMe", None))
        self.webcam_Display.setText(QCoreApplication.translate("FilterMe", u"TextLabel", None))
        self.pushButton_rio.setText(QCoreApplication.translate("FilterMe", u"Rio de Janeiro", None))
        self.pushButton_sketch.setText(QCoreApplication.translate("FilterMe", u"Sketch", None))
        self.pushButton_glasses.setText(QCoreApplication.translate("FilterMe", u"Thug Life", None))
        self.lineEdit_insert_username.setPlaceholderText(QCoreApplication.translate("FilterMe", u"Enter Name Here", None))
        self.pushButton_take_photo_button.setText(QCoreApplication.translate("FilterMe", u"Take Picture", None))
    # retranslateUi

