import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

    def binary(self):
        binary = self.ui.binar.text()
        if
    def octal(self):
        ocal = self.ui.octal.text()
    def decimal(self):
        self.ui.decimal.text()
    def hexadecimal(self):
        self.ui.hexadecimal.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())