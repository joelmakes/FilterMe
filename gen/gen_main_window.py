# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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

class Ui_Filter_Me(object):
    def setupUi(self, Filter_Me):
        if not Filter_Me.objectName():
            Filter_Me.setObjectName(u"Filter_Me")
        Filter_Me.resize(1164, 866)
        Filter_Me.setMinimumSize(QSize(1084, 866))
        Filter_Me.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Filter_Me.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"")
        Filter_Me.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(Filter_Me)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(30, 30, 30, 30)
        self.webcam_Display = QLabel(self.centralwidget)
        self.webcam_Display.setObjectName(u"webcam_Display")
        self.webcam_Display.setAutoFillBackground(False)
        self.webcam_Display.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.webcam_Display)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.widget_main = QWidget(self.centralwidget)
        self.widget_main.setObjectName(u"widget_main")
        self.widget_main.setMaximumSize(QSize(16777215, 200))
        self.widget_main.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.widget_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_buttons = QWidget(self.widget_main)
        self.widget_buttons.setObjectName(u"widget_buttons")
        self.widget_buttons.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_buttons)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.btn_rio = QPushButton(self.widget_buttons)
        self.btn_rio.setObjectName(u"btn_rio")
        self.btn_rio.setMaximumSize(QSize(400, 50))

        self.horizontalLayout.addWidget(self.btn_rio)

        self.btn_sketch = QPushButton(self.widget_buttons)
        self.btn_sketch.setObjectName(u"btn_sketch")
        self.btn_sketch.setMaximumSize(QSize(400, 50))

        self.horizontalLayout.addWidget(self.btn_sketch)

        self.btn_glasses = QPushButton(self.widget_buttons)
        self.btn_glasses.setObjectName(u"btn_glasses")
        self.btn_glasses.setMaximumSize(QSize(400, 50))
        self.btn_glasses.setAutoDefault(False)
        self.btn_glasses.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_glasses)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.widget_buttons)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.insert_username = QLineEdit(self.widget_main)
        self.insert_username.setObjectName(u"insert_username")
        self.insert_username.setMaximumSize(QSize(1300, 100))
        self.insert_username.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.insert_username)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.take_photo_button = QPushButton(self.widget_main)
        self.take_photo_button.setObjectName(u"take_photo_button")
        self.take_photo_button.setMaximumSize(QSize(1300, 40))

        self.horizontalLayout_4.addWidget(self.take_photo_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.widget_main)

        Filter_Me.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Filter_Me)
        self.statusbar.setObjectName(u"statusbar")
        Filter_Me.setStatusBar(self.statusbar)

        self.retranslateUi(Filter_Me)

        self.btn_glasses.setDefault(False)


        QMetaObject.connectSlotsByName(Filter_Me)
    # setupUi

    def retranslateUi(self, Filter_Me):
        Filter_Me.setWindowTitle(QCoreApplication.translate("Filter_Me", u"FilterMe", None))
        self.webcam_Display.setText(QCoreApplication.translate("Filter_Me", u"TextLabel", None))
        self.btn_rio.setText(QCoreApplication.translate("Filter_Me", u"Rio de Janeiro", None))
        self.btn_sketch.setText(QCoreApplication.translate("Filter_Me", u"Sketch", None))
        self.btn_glasses.setText(QCoreApplication.translate("Filter_Me", u"Thug Life", None))
        self.insert_username.setPlaceholderText(QCoreApplication.translate("Filter_Me", u"Enter Name Here", None))
        self.take_photo_button.setText(QCoreApplication.translate("Filter_Me", u"Take Picture", None))
    # retranslateUi

