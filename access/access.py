#!/home/mhamdi/work/dashboard/.venv/bin/python3

import os
import sys

from dotenv import dotenv_values, set_key

from ui_access import *

class Access(Ui_Dialog):
    def __init__(self, Dialog):
        super().setupUi(Dialog)

        self.btn_ok.accepted.connect(self.btn_clicked)
        self.btn_ok.rejected.connect(QCoreApplication.instance().quit)

    def btn_clicked(self):
        username = self.username.toPlainText()
        pwd = self.pwd.toPlainText()

        print(username, pwd)
        # values = dotenv_values('/home/mhamdi/work/prof/.env')  # Load the current .env file
        set_key('/home/mhamdi/work/prof/.env', 'APP_USERNAME', username)
        set_key('/home/mhamdi/work/prof/.env', 'APP_PASSWORD', pwd)

        QCoreApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialogButtonBox()
    ui = Access(Dialog)
    Dialog.show()
    sys.exit(app.exec())