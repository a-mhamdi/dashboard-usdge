# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardejfIEw.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCommandLinkButton, QFrame,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(447, 414)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 90, 441, 261))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.depot = QFrame(self.page_2)
        self.depot.setObjectName(u"depot")
        self.depot.setGeometry(QRect(20, 30, 411, 60))
        self.depot.setFrameShape(QFrame.StyledPanel)
        self.depot.setFrameShadow(QFrame.Raised)
        self.startDepot = QCommandLinkButton(self.depot)
        self.startDepot.setObjectName(u"startDepot")
        self.startDepot.setGeometry(QRect(220, 10, 85, 40))
        self.startDepot.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        self.stopDepot = QPushButton(self.depot)
        self.stopDepot.setObjectName(u"stopDepot")
        self.stopDepot.setGeometry(QRect(310, 10, 85, 40))
        self.stopDepot.setStyleSheet(u"background-color: rgb(220, 50, 47);")
        self.depot_label = QLabel(self.depot)
        self.depot_label.setObjectName(u"depot_label")
        self.depot_label.setGeometry(QRect(10, 0, 131, 50))
        self.depot_label.setFrameShape(QFrame.NoFrame)
        self.portDepot = QTextEdit(self.depot)
        self.portDepot.setObjectName(u"portDepot")
        self.portDepot.setGeometry(QRect(150, 15, 50, 30))
        self.jury = QFrame(self.page_2)
        self.jury.setObjectName(u"jury")
        self.jury.setGeometry(QRect(20, 110, 411, 60))
        self.jury.setFrameShape(QFrame.StyledPanel)
        self.jury.setFrameShadow(QFrame.Raised)
        self.stopJury = QPushButton(self.jury)
        self.stopJury.setObjectName(u"stopJury")
        self.stopJury.setGeometry(QRect(310, 10, 85, 40))
        self.stopJury.setStyleSheet(u"background-color: rgb(220, 50, 47);")
        self.startJury = QCommandLinkButton(self.jury)
        self.startJury.setObjectName(u"startJury")
        self.startJury.setGeometry(QRect(220, 10, 85, 40))
        self.startJury.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        self.jury_label = QLabel(self.jury)
        self.jury_label.setObjectName(u"jury_label")
        self.jury_label.setGeometry(QRect(10, 0, 131, 50))
        self.portJury = QTextEdit(self.jury)
        self.portJury.setObjectName(u"portJury")
        self.portJury.setGeometry(QRect(150, 15, 50, 30))
        self.soutenance = QFrame(self.page_2)
        self.soutenance.setObjectName(u"soutenance")
        self.soutenance.setGeometry(QRect(20, 190, 411, 60))
        self.soutenance.setFrameShape(QFrame.StyledPanel)
        self.soutenance.setFrameShadow(QFrame.Raised)
        self.stopSoutenance = QPushButton(self.soutenance)
        self.stopSoutenance.setObjectName(u"stopSoutenance")
        self.stopSoutenance.setGeometry(QRect(310, 10, 85, 40))
        self.stopSoutenance.setStyleSheet(u"background-color: rgb(220, 50, 47);")
        self.startSoutenance = QCommandLinkButton(self.soutenance)
        self.startSoutenance.setObjectName(u"startSoutenance")
        self.startSoutenance.setGeometry(QRect(220, 10, 85, 40))
        self.startSoutenance.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        self.portSoutenance = QTextEdit(self.soutenance)
        self.portSoutenance.setObjectName(u"portSoutenance")
        self.portSoutenance.setGeometry(QRect(150, 15, 50, 30))
        self.soutenance_label = QLabel(self.soutenance)
        self.soutenance_label.setObjectName(u"soutenance_label")
        self.soutenance_label.setGeometry(QRect(10, 0, 131, 50))
        self.stackedWidget.addWidget(self.page_2)
        self.soutenance.raise_()
        self.jury.raise_()
        self.depot.raise_()
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.calendarWidget = QCalendarWidget(self.page_3)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 76, 421, 171))
        self.email = QFrame(self.page_3)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(9, 20, 421, 51))
        self.email.setFrameShape(QFrame.StyledPanel)
        self.email.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.email)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 171, 51))
        self.init = QRadioButton(self.email)
        self.init.setObjectName(u"init")
        self.init.setGeometry(QRect(230, 10, 41, 30))
        self.init.setStyleSheet(u"background-color: rgb(249, 240, 107);\n"
"color: rgb(0, 0, 0);")
        self.perf = QRadioButton(self.email)
        self.perf.setObjectName(u"perf")
        self.perf.setGeometry(QRect(280, 10, 41, 30))
        self.perf.setStyleSheet(u"background-color: rgb(38, 162, 105);\n"
"color: rgb(0, 0, 0);")
        self.envoyer = QPushButton(self.email)
        self.envoyer.setObjectName(u"envoyer")
        self.envoyer.setGeometry(QRect(340, 10, 71, 31))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.calendarWidget_2 = QCalendarWidget(self.page_4)
        self.calendarWidget_2.setObjectName(u"calendarWidget_2")
        self.calendarWidget_2.setGeometry(QRect(10, 76, 421, 171))
        self.email_2 = QFrame(self.page_4)
        self.email_2.setObjectName(u"email_2")
        self.email_2.setGeometry(QRect(10, 20, 420, 51))
        self.email_2.setFrameShape(QFrame.StyledPanel)
        self.email_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.email_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 171, 51))
        self.init_2 = QRadioButton(self.email_2)
        self.init_2.setObjectName(u"init_2")
        self.init_2.setGeometry(QRect(230, 10, 41, 30))
        self.init_2.setStyleSheet(u"background-color: rgb(249, 240, 107);\n"
"color: rgb(0, 0, 0);")
        self.perf_2 = QRadioButton(self.email_2)
        self.perf_2.setObjectName(u"perf_2")
        self.perf_2.setGeometry(QRect(280, 10, 41, 30))
        self.perf_2.setStyleSheet(u"background-color: rgb(38, 162, 105);\n"
"color: rgb(0, 0, 0);")
        self.pushButton = QPushButton(self.email_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 10, 71, 31))
        self.stackedWidget.addWidget(self.page_4)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 340, 181, 61))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 350, 41, 41))
        self.label_7.setPixmap(QPixmap(u"ISETBZ.png"))
        self.label_7.setScaledContents(True)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 10, 441, 71))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.startDepot.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-style:italic;\">D\u00e9marrer le serveur de d\u00e9p\u00f4t des rapports.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.startDepot.setText(QCoreApplication.translate("MainWindow", u"D\u00e9marrer", None))
        self.stopDepot.setText(QCoreApplication.translate("MainWindow", u"Arr\u00eater", None))
        self.depot_label.setText(QCoreApplication.translate("MainWindow", u"D\u00e9p\u00f4t des rapports", None))
        self.portDepot.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Delicious Heavy'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PORT</p></body></html>", None))
        self.stopJury.setText(QCoreApplication.translate("MainWindow", u"Arr\u00eater", None))
#if QT_CONFIG(tooltip)
        self.startJury.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-style:italic;\">Affecter les membres de jury.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.startJury.setText(QCoreApplication.translate("MainWindow", u"D\u00e9marrer", None))
        self.jury_label.setText(QCoreApplication.translate("MainWindow", u"Affectation du jury", None))
        self.portJury.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Delicious Heavy'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PORT</p></body></html>", None))
        self.stopSoutenance.setText(QCoreApplication.translate("MainWindow", u"Arr\u00eater", None))
#if QT_CONFIG(tooltip)
        self.startSoutenance.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>D\u00e9marrer les soutenances.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.startSoutenance.setText(QCoreApplication.translate("MainWindow", u"D\u00e9marrer", None))
        self.portSoutenance.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Delicious Heavy'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PORT</p></body></html>", None))
        self.soutenance_label.setText(QCoreApplication.translate("MainWindow", u"Portail d'\u00e9valuation", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Zipper et envoyer e-mails", None))
        self.init.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.perf.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.envoyer.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rer les pvs", None))
        self.init_2.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.perf_2.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-style:italic; color:#1a5fb4;\">ISET de Bizerte<br/>D\u00e9partement de g\u00e9nie \u00e9lectrique<br/>Unit\u00e9 des stages</span></p></body></html>", None))
        self.label_7.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Montserrat','sans-serif'; font-size:36px; color:#ffffff; text-transform:uppercase;\">Gestion des stages </span></p></body></html>", None))
    # retranslateUi

