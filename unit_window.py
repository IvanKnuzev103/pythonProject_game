import mouse
import pygame
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from pynput import mouse

def go(sc):
    x, y = pygame.mouse.get_pos()
    pygame.draw.rect(sc, 'green', ((x // 40 * 40), (y // 40 * 40), 40, 40), 5)



class MyWidget_1(QDialog):
    def __init__(self, tit, ui, par, pos, screen_2):
        super().__init__()
        self.setWindowTitle('Give the order my lord')
        uic.loadUi(ui, self)
        self.button_bathe.clicked.connect(lambda: self.bathe(par))
        self.fight_button.clicked.connect(self.fight)
        self.move_button.clicked.connect(lambda: self.move_1(pos, screen_2))

    def move_1(self, pos, screen_2):
        self.close()
        return go(screen_2)

    def fight(self):
        self.close()

    def bathe(self, n):
        self.close()
        n[3] = ('bathe', 'yes')
        return n
