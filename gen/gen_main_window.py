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

class Ui_Filter_Me(object):
    def setupUi(self, Filter_Me):
        if not Filter_Me.objectName():
            Filter_Me.setObjectName(u"Filter_Me")
        Filter_Me.resize(1084, 866)
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
        self.webcam_Display = QLabel(self.centralwidget)
        self.webcam_Display.setObjectName(u"webcam_Display")

        self.verticalLayout.addWidget(self.webcam_Display)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_rio = QPushButton(self.centralwidget)
        self.btn_rio.setObjectName(u"btn_rio")

        self.horizontalLayout.addWidget(self.btn_rio)

        self.btn_sketch = QPushButton(self.centralwidget)
        self.btn_sketch.setObjectName(u"btn_sketch")

        self.horizontalLayout.addWidget(self.btn_sketch)

        self.btn_glasses = QPushButton(self.centralwidget)
        self.btn_glasses.setObjectName(u"btn_glasses")
        self.btn_glasses.setAutoDefault(False)
        self.btn_glasses.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_glasses)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.insert_username = QLineEdit(self.centralwidget)
        self.insert_username.setObjectName(u"insert_username")
        self.insert_username.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.insert_username, 0, Qt.AlignmentFlag.AlignVCenter)

        self.take_photo_button = QPushButton(self.centralwidget)
        self.take_photo_button.setObjectName(u"take_photo_button")

        self.verticalLayout_2.addWidget(self.take_photo_button)


        self.verticalLayout.addLayout(self.verticalLayout_2)

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
        self.btn_glasses.setText(QCoreApplication.translate("Filter_Me", u"Bug Life", None))
        self.insert_username.setPlaceholderText(QCoreApplication.translate("Filter_Me", u"Enter Name Here", None))
        self.take_photo_button.setText(QCoreApplication.translate("Filter_Me", u"Take Picture", None))
    # retranslateUi

