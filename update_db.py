#! .venv/bin/python3

import os, sys
import pymongo
from pymongo import MongoClient

# from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

from ui_update_db import *

num_cin = ''


class UpdateDB(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)

        ## DB Setup
        connection = MongoClient('localhost', 27017)
        db = connection['dept-ge']
        self.students = db['students']
        self.cursor = None

        self.get_cin.clicked.connect(self.get_cin_clicked)
        self.edit_db.clicked.connect(self.edit_db_clicked)

    def get_cin_clicked(self):
        try:
            global num_cin
            num_cin = self.cin.toPlainText()
            self.cursor = self.students.find({'cin': num_cin})
            x = list(self.cursor)
            name = x[0]['name']
            self.student.setText(name)
            attestation_st = x[0]['piecesManquantes']['attestation']
            if  attestation_st == 'manquante':
                self.manquante.setChecked(True)
                self.presente.setChecked(False)
            else:
                self.manquante.setChecked(False)
                self.presente.setChecked(True)
            initiation = x[0]['initiation']
            perfectionnement = x[0]['perfectionnement']
            self.note_initiation.setText(str(initiation))
            self.note_perfectionnement.setText(str(perfectionnement))
        except Exception as e:
            print(e)

    def edit_db_clicked(self):
        self.students.update_one({"cin": num_cin}, {"$set": { \
            "piecesManquantes": "Presente", \
            "initiation.score": 10, \
            "initiation.isLocked": True, \
            "perfectionnement.score": 10, \
            "perfectionnement.isLocked": True \
        }})


def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = UpdateDB(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()
"""
if __name__ == '__main__':
    main()
"""