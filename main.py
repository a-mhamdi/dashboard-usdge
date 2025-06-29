#!/home/mhamdi/work/dashboard/.venv/bin/python3

import os
import sys
import subprocess

from dotenv import dotenv_values, set_key

from ui_dashboard import *

pm2_path = '/home/mhamdi/.nvm/versions/node/v20.17.0/bin/pm2'

class Dashboard(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)

        self.pages.setCurrentIndex(0)
        self.btn1.hide()

        self.btn1.clicked.connect(self.page1_loader)
        self.btn2.clicked.connect(self.page2_loader)
        self.btn3.clicked.connect(self.page3_loader)

        # DEPOT
        self.startDepot.clicked.connect(self.start_depot_clicked)
        self.stopDepot.clicked.connect(self.stop_depot_clicked)
        # JURY
        self.startJury.clicked.connect(self.start_jury_clicked)
        self.stopJury.clicked.connect(self.stop_jury_clicked)
        # SOUTENANCE
        self.startSoutenance.clicked.connect(self.start_soutenance_clicked)
        self.stopSoutenance.clicked.connect(self.stop_soutenance_clicked)
        # ZIPPER
        self.zipper.clicked.connect(self.zipper_fichiers)
        # PVS
        self.pv_btn.clicked.connect(self.generer_pvs)
        # UPDATE DB
        self.updatedb.clicked.connect(self.update_db)

    def page1_loader(self):
        self.pages.setCurrentIndex(0)
        self.btn1.hide()
        self.btn2.show()
        self.btn3.show()

    def page2_loader(self):
        self.pages.setCurrentIndex(1)
        self.btn1.show()
        self.btn2.hide()
        self.btn3.show()

    def page3_loader(self):
        self.pages.setCurrentIndex(2)
        self.btn1.show()
        self.btn2.show()
        self.btn3.hide()

    def start_depot_clicked(self):
        # self.startDepot.hide()
        command = ["pm2", "start"]
        os.chdir("/home/mhamdi/work/etudiant")
        port = self.portDepot.toPlainText()
        if port == 'PORT':
            values = dotenv_values('.env')  # Load the current .env file
            msg = f"Port is set to {values['APP_PORT']}"
            subprocess.run(
                ['zenity', '--info', '--text', msg])
        else:
            set_key('.env', 'APP_PORT', port)
        subprocess.run(command)

    def stop_depot_clicked(self):
        # self.startDepot.show()
        command = ["pm2", "stop", "Dépôt"]
        os.chdir("/home/mhamdi/work/etudiant")
        subprocess.run(command)

    def start_jury_clicked(self):
        # self.startDepot.hide()
        command = ["pm2", "start"]
        os.chdir("/home/mhamdi/work/affectation-jury")
        port = self.portJury.toPlainText()
        if port == 'PORT':
            values = dotenv_values('.env')  # Load the current .env file
            msg = f"Port is set to {values['APP_PORT']}"
            subprocess.run(
                ['zenity', '--info', '--text', msg])
        else:
            set_key('.env', 'APP_PORT', port)
        subprocess.run(command)

    def stop_jury_clicked(self):
        # self.startDepot.show()
        command = ["pm2", "stop", "Jury"]
        os.chdir("/home/mhamdi/work/affectation-jury")
        subprocess.run(command)

    def start_soutenance_clicked(self):
        # self.startDepot.hide()
        subprocess.run(["bash", "-c", "/home/mhamdi/work/dashboard/access/access.py"])
        command = ["pm2", "start"]
        os.chdir("/home/mhamdi/work/prof")
        port = self.portSoutenance.toPlainText()
        if port == 'PORT':
            values = dotenv_values('.env')  # Load the current .env file
            msg = f"Port is set to {values['APP_PORT']}"
            subprocess.run(
                ['zenity', '--info', '--text', msg])
        else:
            set_key('.env', 'APP_PORT', port)
        subprocess.run(command)

    def stop_soutenance_clicked(self):
        # self.startDepot.show()
        command = ["pm2", "stop", "Évaluation"]
        os.chdir("/home/mhamdi/work/prof")
        subprocess.run(command)

    def zipper_fichiers(self):
        type = 'init'
        if self.perf.isChecked():
            type = 'perf'
        date = self.calendarWidget.selectedDate().toString("dd-MM-yyyy")
        zippedFiles = f"/home/mhamdi/work/dashboard/zip_per_prof.py {type} {date}"
        subprocess.run(["bash", "-c", zippedFiles])

    def generer_pvs(self):
        os.chdir("/home/mhamdi/work/pvs")
        type = 'init'
        if self.perf_2.isChecked():
            type = 'perf'
        date = self.calendarWidget_2.selectedDate().toString("dd/MM/yyyy")
        command = f'/home/mhamdi/work/pvs/pdf_generator.sh {type} {date}'
        subprocess.run(["bash", "-c", command])
        folder_to_open = 'xdg-open /home/mhamdi/Desktop/PVS'
        subprocess.run(["bash", "-c", folder_to_open])

    def update_db(self):
        subprocess.run(["bash", "-c", "./update_db.py"])
        # updatedb = QApplication(sys.argv)
        #updatedb_window = QMainWindow()
        #ui_updatedb = UpdateDB(updatedb_window)
        #updatedb_window.show()
        #sys.exit(updatedb_window.exec_())

def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Dashboard(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
