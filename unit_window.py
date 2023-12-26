import pygame
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog


class MyWidget_1(QDialog):
    def __init__(self, tit, ui, par, pos):
        super().__init__()
        self.setWindowTitle('Give the order my lord')
        uic.loadUi(ui, self)
        self.button_bathe.clicked.connect(lambda: self.bathe(par))
        self.fight_button.clicked.connect(self.fight)
        self.move_button.clicked.connect(lambda : self.move_1(pos))

    def move_1(self, pos):
        print(pos)
        x, y = pygame.mouse.get_pos()
        print(x, y)
        self.close()

    def fight(self):
        self.close()

    def bathe(self, n):
        self.close()
        n[3] = ('bathe', 'yes')
        return n
