# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_dbthqimI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(536, 475)
        self.cin = QTextEdit(MainWindow)
        self.cin.setObjectName(u"cin")
        self.cin.setGeometry(QRect(20, 60, 131, 31))
        self.get_cin = QPushButton(MainWindow)
        self.get_cin.setObjectName(u"get_cin")
        self.get_cin.setGeometry(QRect(180, 60, 89, 25))
        self.etudiant = QLabel(MainWindow)
        self.etudiant.setObjectName(u"etudiant")
        self.etudiant.setGeometry(QRect(30, 110, 61, 21))
        self.student = QLabel(MainWindow)
        self.student.setObjectName(u"student")
        self.student.setGeometry(QRect(160, 110, 111, 17))
        self.tabWidget = QTabWidget(MainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(30, 230, 421, 201))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.note_initiation = QLineEdit(self.tab)
        self.note_initiation.setObjectName(u"note_initiation")
        self.note_initiation.setGeometry(QRect(240, 20, 161, 31))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.note_perfectionnement = QLineEdit(self.tab_2)
        self.note_perfectionnement.setObjectName(u"note_perfectionnement")
        self.note_perfectionnement.setGeometry(QRect(40, 30, 351, 121))
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 140, 91, 17))
        self.presente = QRadioButton(MainWindow)
        self.presente.setObjectName(u"presente")
        self.presente.setGeometry(QRect(170, 140, 112, 23))
        self.manquante = QRadioButton(MainWindow)
        self.manquante.setObjectName(u"manquante")
        self.manquante.setGeometry(QRect(290, 140, 112, 23))
        self.edit_db = QPushButton(MainWindow)
        self.edit_db.setObjectName(u"edit_db")
        self.edit_db.setGeometry(QRect(290, 60, 89, 25))

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Update dB", None))
        self.get_cin.setText(QCoreApplication.translate("MainWindow", u"R\u00e9cuperez", None))
        self.etudiant.setText(QCoreApplication.translate("MainWindow", u"Etudiant", None))
        self.student.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Initiation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Perfectionnement", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Attestation", None))
        self.presente.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.manquante.setText(QCoreApplication.translate("MainWindow", u"Manquante", None))
        self.edit_db.setText(QCoreApplication.translate("MainWindow", u"Modifiez", None))
    # retranslateUi

