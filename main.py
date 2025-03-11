import os
import sys
import subprocess

from dotenv import dotenv_values, set_key

from ui_dashboard import *


class Dashboard(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        # DEPOT
        self.startDepot.clicked.connect(self.start_depot_clicked)
        self.stopDepot.clicked.connect(self.stop_depot_clicked)
        # JURY
        self.startJury.clicked.connect(self.start_jury_clicked)
        self.stopJury.clicked.connect(self.stop_jury_clicked)
        # SOUTENANCE
        self.startSoutenance.clicked.connect(self.start_soutenance_clicked)
        self.stopSoutenance.clicked.connect(self.stop_soutenance_clicked)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Dashboard(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
