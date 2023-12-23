import sys
from random import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class MyWidget(QMainWindow):
    def __init__(self, tit, ui):
        super().__init__()
        self.setWindowTitle('Give the order my lord')
        uic.loadUi(ui, self)
        self.button_bathe.clicked.connect(self.bathe)
        self.fight_button.clicked.connect(self.fight)
        self.move_button.clicked.connect(self.move_1)



    def move_1(self):
       self.destroyed()

    def fight(self):
        self.destroyed()

    def bathe(self):
        self.destroyed()

