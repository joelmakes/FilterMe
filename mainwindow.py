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

class Ui_Joel_Task(object):
    def setupUi(self, Joel_Task):
        if not Joel_Task.objectName():
            Joel_Task.setObjectName(u"Joel_Task")
        Joel_Task.resize(1084, 866)
        Joel_Task.setMinimumSize(QSize(1084, 866))
        Joel_Task.setStyleSheet(u"background-color: #2b2b2b;\n"
"color: white;\n"
"")
        Joel_Task.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(Joel_Task)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 580, 1091, 111))
        self.horizontalLayout = QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_rio = QPushButton(self.verticalLayoutWidget)
        self.btn_rio.setObjectName(u"btn_rio")

        self.horizontalLayout.addWidget(self.btn_rio)

        self.btn_sketch = QPushButton(self.verticalLayoutWidget)
        self.btn_sketch.setObjectName(u"btn_sketch")

        self.horizontalLayout.addWidget(self.btn_sketch)

        self.btn_glasses = QPushButton(self.verticalLayoutWidget)
        self.btn_glasses.setObjectName(u"btn_glasses")

        self.horizontalLayout.addWidget(self.btn_glasses)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 690, 1081, 161))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.insert_username = QLineEdit(self.verticalLayoutWidget_2)
        self.insert_username.setObjectName(u"insert_username")

        self.verticalLayout_2.addWidget(self.insert_username)

        self.take_photo_button = QPushButton(self.verticalLayoutWidget_2)
        self.take_photo_button.setObjectName(u"take_photo_button")

        self.verticalLayout_2.addWidget(self.take_photo_button)

        self.webcam_Display = QLabel(self.centralwidget)
        self.webcam_Display.setObjectName(u"webcam_Display")
        self.webcam_Display.setGeometry(QRect(18, 15, 1041, 561))
        Joel_Task.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Joel_Task)
        self.statusbar.setObjectName(u"statusbar")
        Joel_Task.setStatusBar(self.statusbar)

        self.retranslateUi(Joel_Task)

        QMetaObject.connectSlotsByName(Joel_Task)
    # setupUi

    def retranslateUi(self, Joel_Task):
        Joel_Task.setWindowTitle(QCoreApplication.translate("Joel_Task", u"FilterMe", None))
        self.btn_rio.setText(QCoreApplication.translate("Joel_Task", u"Rio de Janeiro", None))
        self.btn_sketch.setText(QCoreApplication.translate("Joel_Task", u"Sketch", None))
        self.btn_glasses.setText(QCoreApplication.translate("Joel_Task", u"Thug Life", None))
        self.take_photo_button.setText(QCoreApplication.translate("Joel_Task", u"Take Picture", None))
        self.webcam_Display.setText(QCoreApplication.translate("Joel_Task", u"TextLabel", None))
    # retranslateUi

