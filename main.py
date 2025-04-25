import sys

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.change.clicked.connect(self.binary)
        self.ui.change.clicked.connect(self.octal)
        self.ui.change.clicked.connect(self.decimal)
        self.ui.change.clicked.connect(self.hexadecimal)
        self.show()

    def binary(self):
        binary = self.ui.binar.text()
        bin(int(binary, 2))
        if not (c in '01' for c in binary):
            print("Bład binarny")

    def octal(self):
        octal = self.ui.octal.text()
        oct(int(octal, 8))
        if not (c in '01234567' for c in octal):
            print("Błąd ósemkowy")

    def decimal(self):
        decimal = self.ui.decimal.text()
        int(decimal, 10)
        if not decimal.isdigit():
            print("Błąd dziesiątkowy")

    def hexadecimal(self):
        hexadecimal = self.ui.hexadecimal.text()
        hex(int(hexadecimal, 16))
        if not int:
            print("Błąd szesnastkowy")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())