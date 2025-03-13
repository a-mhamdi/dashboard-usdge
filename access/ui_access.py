# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accessrkNqeP.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(317, 97)
        self.btn_ok = QDialogButtonBox(Dialog)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(220, 20, 81, 241))
        self.btn_ok.setOrientation(Qt.Vertical)
        self.btn_ok.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 81, 20))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 60, 41, 19))
        self.username = QTextEdit(Dialog)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(100, 20, 111, 31))
        self.username.setStyleSheet(u"")
        self.pwd = QTextEdit(Dialog)
        self.pwd.setObjectName(u"pwd")
        self.pwd.setGeometry(QRect(100, 60, 111, 31))

        self.retranslateUi(Dialog)
        # self.btn_ok.accepted.connect(Dialog.accept)
        # self.btn_ok.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Acc\u00e8s", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"USERNAME", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"PWD", None))
    # retranslateUi

