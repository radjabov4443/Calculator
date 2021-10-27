import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class mainWindow(QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.view()

    def view(self):
        self.setFixedSize(232, 292)
        # self.setGeometry(100, 100, 360, 350)

        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.h_box5 = QHBoxLayout()
        self.v_box = QVBoxLayout()

        self.label = QLabel()
        # self.label.setGeometry(5, 5, 350, 70)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel""{""border : 2px solid black;""background : dark;""}")
        self.label.setAlignment(Qt.AlignRight)

        self.btn_numbers = list()
        self.btn_plus = QPushButton("+")
        self.btn_minus = QPushButton("-")
        self.btn_mul = QPushButton("*")
        self.btn_equal = QPushButton("=")
        self.btn_dist = QPushButton("/")
        self.btn_point = QPushButton(".")
        self.btn_del = QPushButton("Del")
        self.btn_clear = QPushButton("C")
        for i in range(0, 10):
            self.btn_numbers.append(QPushButton(f"{i}"))

        self.h_box1.addWidget(self.btn_clear)
        self.h_box1.addWidget(self.btn_del)

        for i in range(1, 5):
            if i == 4:
                self.h_box2.addWidget(self.btn_plus)
            else:
                self.h_box2.addWidget(self.btn_numbers[i])

        for i in range(4, 8):
            if i == 7:
                self.h_box3.addWidget(self.btn_minus)
            else:
                self.h_box3.addWidget(self.btn_numbers[i])

        for i in range(7, 11):
            if i == 10:
                self.h_box4.addWidget(self.btn_mul)
            else:
                self.h_box4.addWidget(self.btn_numbers[i])

        self.h_box5.addWidget(self.btn_point)
        self.h_box5.addWidget(self.btn_numbers[0])
        self.h_box5.addWidget(self.btn_dist)
        self.h_box5.addWidget(self.btn_equal)

        self.v_box.addWidget(self.label)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box5)

        self.setLayout(self.v_box)

        self.btn_numbers[0].clicked.connect(self.action0)
        self.btn_numbers[1].clicked.connect(self.action1)
        self.btn_numbers[2].clicked.connect(self.action2)
        self.btn_numbers[3].clicked.connect(self.action3)
        self.btn_numbers[4].clicked.connect(self.action4)
        self.btn_numbers[5].clicked.connect(self.action5)
        self.btn_numbers[6].clicked.connect(self.action6)
        self.btn_numbers[7].clicked.connect(self.action7)
        self.btn_numbers[8].clicked.connect(self.action8)
        self.btn_numbers[9].clicked.connect(self.action9)

        self.btn_equal.clicked.connect(self.action_equal)
        self.btn_mul.clicked.connect(self.action_mul)
        self.btn_del.clicked.connect(self.action_del)
        self.btn_dist.clicked.connect(self.action_dist)
        self.btn_point.clicked.connect(self.action_point)
        self.btn_minus.clicked.connect(self.action_minus)
        self.btn_plus.clicked.connect(self.action_plus)
        self.btn_clear.clicked.connect(self.action_clear)

    def action_equal(self):
        equ = self.label.text()
        try:
            args = eval(equ)
            self.label.setText(str(args))
        except:
            self.label.setText("Wrong Input!")

    def action_plus(self):
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_minus(self):
        text = self.label.text()
        self.label.setText(text + " - ")

    def action_dist(self):
        text = self.label.text()
        self.label.setText(text + " / ")

    def action_mul(self):
        text = self.label.text()
        self.label.setText(text + " * ")

    def action_point(self):
        text = self.label.text()
        self.label.setText(text + ".")

    def action0(self):
        text = self.label.text()
        self.label.setText(text + "0")

    def action1(self):
        text = self.label.text()
        self.label.setText(text + "1")

    def action2(self):
        text = self.label.text()
        self.label.setText(text + "2")

    def action3(self):
        text = self.label.text()
        self.label.setText(text + "3")

    def action4(self):
        text = self.label.text()
        self.label.setText(text + "4")

    def action5(self):
        text = self.label.text()
        self.label.setText(text + "5")

    def action6(self):
        text = self.label.text()
        self.label.setText(text + "6")

    def action7(self):
        text = self.label.text()
        self.label.setText(text + "7")

    def action8(self):
        text = self.label.text()
        self.label.setText(text + "8")

    def action9(self):
        text = self.label.text()
        self.label.setText(text + "9")

    def action_clear(self):
        self.label.setText("")

    def action_del(self):
        text = self.label.text()
        print(text[:len(text) - 1])
        self.label.setText(text[:len(text) - 1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())
