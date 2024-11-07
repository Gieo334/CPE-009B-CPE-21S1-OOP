import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit, QPushButton, QGridLayout, QGroupBox, QHBoxLayout, QVBoxLayout, QTextEdit)
from PyQt5.QtGui import QIcon

class Click(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Midterm Examination"
        self.x = 300
        self.y = 300
        self.width = 400
        self.height = 350
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.createGridLayout()
        self.setLayout(self.layout)
        self.show()

    def createGridLayout(self):
        self.layout = QGridLayout()
        self.button = QPushButton("Click to Change Color", self)
        self.button.clicked.connect(self.changeColor)
        self.layout.addWidget(self.button, 2, 2)

    def changeColor(self):
        self.button.setStyleSheet("background-color:blue")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Click()
    sys.exit(app.exec_())
