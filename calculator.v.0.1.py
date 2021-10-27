import PyQt5
from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.view()

    def view(self):
        self.setFixedSize(300, 400)
        self.btn1 = QPushButton("1", self)
        self.btn2 = QPushButton("2", self)
        self.equal = QPushButton("=", self)
        self.plus = QPushButton("+", self)
        self.backspace = QPushButton("<-", self)
        self.label = QLabel("Result", self)
        self.label.move(90, 20)
        self.equal.move(90, 70)
        self.btn1.move(30, 40)
        self.btn2.move(150, 40)
        self.plus.move(90, 100)

        self.plus.clicked.connect(self.add)
        self.btn1.clicked.connect(self.one)
        self.btn2.clicked.connect(self.two)
        self.equal.clicked.connect(self.equal1)
        self.backspace.clicked.connect(self.del_item)

    sum = ""

    def add(self):
        self.sum += "+"
        self.label.setText(self.sum)
        self.label.adjustSize()

    def one(self):
        self.sum += "1"
        self.label.setText(self.sum)
        self.label.adjustSize()

    def two(self):
        self.sum += "2"
        self.label.setText(self.sum)
        self.label.adjustSize()

    def equal1(self):
        result = str(eval(self.sum))
        self.label.setText(result)
        self.label.adjustSize()

    def del_item(self):
        st = ""
        for i in range(0, len(self.sum) - 1):
            st += self.sum[i]
        self.sum = st
        self.label.setText(self.sum)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
