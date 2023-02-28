# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dopasowanie_match3.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class guiBoard(object):
    def setupUi(self, Dopasowanie_match3):
        if not Dopasowanie_match3.objectName():
            Dopasowanie_match3.setObjectName(u"Dopasowanie_match3")
        Dopasowanie_match3.resize(671, 150)
        self.centralwidget = QWidget(Dopasowanie_match3)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tekst_szerokosc = QLabel(self.centralwidget)
        self.tekst_szerokosc.setObjectName(u"tekst_szerokosc")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tekst_szerokosc.setFont(font)

        self.verticalLayout.addWidget(self.tekst_szerokosc)

        self.tekst_wysokosc = QLabel(self.centralwidget)
        self.tekst_wysokosc.setObjectName(u"tekst_wysokosc")
        self.tekst_wysokosc.setFont(font)

        self.verticalLayout.addWidget(self.tekst_wysokosc)

        self.tekst_rodzaje = QLabel(self.centralwidget)
        self.tekst_rodzaje.setObjectName(u"tekst_rodzaje")
        self.tekst_rodzaje.setFont(font)

        self.verticalLayout.addWidget(self.tekst_rodzaje)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.slider_szerokosc = QSlider(self.centralwidget)
        self.slider_szerokosc.setObjectName(u"slider_szerokosc")
        self.slider_szerokosc.setMinimum(5)
        self.slider_szerokosc.setMaximum(12)
        self.slider_szerokosc.setSliderPosition(8)
        self.slider_szerokosc.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_szerokosc)

        self.slider_wysokosc = QSlider(self.centralwidget)
        self.slider_wysokosc.setObjectName(u"slider_wysokosc")
        self.slider_wysokosc.setMinimum(5)
        self.slider_wysokosc.setMaximum(12)
        self.slider_wysokosc.setSliderPosition(8)
        self.slider_wysokosc.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_wysokosc)

        self.slider_rodzaje = QSlider(self.centralwidget)
        self.slider_rodzaje.setObjectName(u"slider_rodzaje")
        self.slider_rodzaje.setMinimum(5)
        self.slider_rodzaje.setMaximum(10)
        self.slider_rodzaje.setSliderPosition(7)
        self.slider_rodzaje.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_rodzaje)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.spin_szerokosc = QSpinBox(self.centralwidget)
        self.spin_szerokosc.setObjectName(u"spin_szerokosc")
        self.spin_szerokosc.setMinimum(3)
        self.spin_szerokosc.setMaximum(12)
        self.spin_szerokosc.setValue(8)

        self.verticalLayout_3.addWidget(self.spin_szerokosc)

        self.spin_wysokosc = QSpinBox(self.centralwidget)
        self.spin_wysokosc.setObjectName(u"spin_wysokosc")
        self.spin_wysokosc.setMinimum(3)
        self.spin_wysokosc.setMaximum(12)
        self.spin_wysokosc.setValue(8)

        self.verticalLayout_3.addWidget(self.spin_wysokosc)

        self.spin_rodzaje = QSpinBox(self.centralwidget)
        self.spin_rodzaje.setObjectName(u"spin_rodzaje")
        self.spin_rodzaje.setMinimum(3)
        self.spin_rodzaje.setMaximum(10)
        self.spin_rodzaje.setValue(7)

        self.verticalLayout_3.addWidget(self.spin_rodzaje)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.button_play = QPushButton(self.centralwidget)
        self.button_play.setObjectName(u"button_play")
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        self.button_play.setFont(font1)

        self.verticalLayout_4.addWidget(self.button_play)

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        Dopasowanie_match3.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Dopasowanie_match3)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 671, 30))
        Dopasowanie_match3.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Dopasowanie_match3)
        self.statusbar.setObjectName(u"statusbar")
        Dopasowanie_match3.setStatusBar(self.statusbar)

        self.retranslateUi(Dopasowanie_match3)

        QMetaObject.connectSlotsByName(Dopasowanie_match3)
    # setupUi

    def retranslateUi(self, Dopasowanie_match3):
        Dopasowanie_match3.setWindowTitle(QCoreApplication.translate("Dopasowanie_match3", u"MainWindow", None))
        self.tekst_szerokosc.setText(QCoreApplication.translate("Dopasowanie_match3", u"Podaj szeroko\u015b\u0107 planszy: ", None))
        self.tekst_wysokosc.setText(QCoreApplication.translate("Dopasowanie_match3", u"Podaj wysoko\u015b\u0107 planszy: ", None))
        self.tekst_rodzaje.setText(QCoreApplication.translate("Dopasowanie_match3", u"Podaj ilo\u015b\u0107 rodzaj\u00f3w blok\u00f3w: ", None))
        self.button_play.setText(QCoreApplication.translate("Dopasowanie_match3", u"Graj", None))
    # retranslateUi

