import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.h_box = QHBoxLayout()
        self.h_box1 = QHBoxLayout()
        self.v_box = QVBoxLayout()
        self.label = QLabel()
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.btn1 = QPushButton("+")
        self.btn2 = QPushButton("-")
        self.btn3 = QPushButton("*")
        self.btn4 = QPushButton("/")

        self.v_box.addWidget(self.label)
        self.h_box.addWidget(self.edit1)
        self.h_box.addWidget(self.edit2)
        self.h_box1.addWidget(self.btn1)
        self.h_box1.addWidget(self.btn2)
        self.h_box1.addWidget(self.btn3)
        self.h_box1.addWidget(self.btn4)
        self.v_box.addLayout(self.h_box)
        self.v_box.addLayout(self.h_box1)

        self.btn1.clicked.connect(lambda: self.sum("+"))
        self.btn2.clicked.connect(lambda: self.sum("-"))
        self.btn3.clicked.connect(lambda: self.sum("*"))
        self.btn4.clicked.connect(lambda: self.sum("/"))

        self.setLayout(self.v_box)
        self.show()

    def sum(self, op):
        try:
            a = int(self.edit1.text())
            b = int(self.edit2.text())

            if op == "+":
                self.label.setText(f"{a + b}")
            elif op == "-":
                self.label.setText(f"{a - b}")
            elif op == "*":
                self.label.setText(f"{a * b}")
            elif op == "/":
                self.label.setText(f"{a / b}")
        except ValueError:
            self.label.setText("Iltimos, faqat son kiriting!")

        self.edit1.clear()
        self.edit2.clear()


if __name__ == "__main__":
    app = QApplication([])
    win = mainWindow()
    sys.exit(app.exec_())
