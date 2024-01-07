import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog

import class_Main_building
import class_resurs_gold
import class_resurs_iron
import class_resurs_wood
import class_unit_all
from class_random_resurs_in_map import clear
from class_unit_all import *

global screen


def go(sc, pos, n):
    old_data = (open('map_game', 'r')).readlines()
    x, y = pygame.mouse.get_pos()
    if (old_data[y // 50][x // 50]) == '.' and (pos[0] + 2 >= x // 50 >= pos[0] - 2) and (
            pos[1] + 2 >= y // 50 >= pos[1] - 2):
        pygame.draw.rect(sc, 'green', ((x // 50 * 50), (y // 50 * 50), 50, 50), 5)
        old_data[y // 50] = (
                (old_data[y // 50])[:x // 50] + str((old_data[pos[1]])[pos[0]]) + old_data[y // 50][x // 50 + 1:])
        old_data[pos[1]] = ((old_data[pos[1]])[:pos[0]] + '.' + old_data[pos[1]][pos[0] + 1:])
        new_data = open('map_game', 'w')
        for elem in old_data:
            new_data.write(elem)
    else:
        x, y = pygame.mouse.get_pos()
        pygame.draw.rect(sc, 'red', ((x // 50 * 50), (y // 50 * 50), 50, 50), 20)


def con(sc, pos, n, par):
    old_data = (open('map_game', 'r')).readlines()
    A = {'M': 'm', 'i': 'm', 'g': 'z', 'Z': 'z', 'w': 'd', 'D': 'd'}
    B = {'m': 'M', 'i': 'M', 'g': 'Z', 'z': 'Z', 'w': 'D', 'd': 'D'}
    x, y = pygame.mouse.get_pos()

    if (old_data[y // 50][x // 50] != '.' and (old_data[y // 50][x // 50]) != '@' and (
            old_data[y // 50][x // 50]) != '#' and (old_data[y // 50][x // 50]) != 'u' and (
                old_data[y // 50][x // 50]) != '@' and (old_data[y // 50][x // 50]) != 'U') and (
            pos[0] + 2 >= x // 50 >= pos[0] - 2) and (
            pos[1] + 2 >= y // 50 >= pos[1] - 2):
        if par[1][1] == 'left' and old_data[y // 50][x // 50] != 'z' and old_data[y // 50][x // 50] != 'd' and \
                old_data[y // 50][x // 50] != 'm':
            old_data[y // 50] = str(old_data[y // 50])[:x // 50] + A[old_data[y // 50][x // 50]] + old_data[y // 50][
                                                                                                   x // 50 + 1:]
            new_data = open('map_game', 'w')
            for elem in old_data:
                new_data.write(elem)
        elif par[1][1] == 'right' and old_data[y // 50][x // 50] != 'Z' and old_data[y // 50][x // 50] != 'D' and \
                old_data[y // 50][x // 50] != 'M':
            old_data[y // 50] = str(old_data[y // 50])[:x // 50] + B[old_data[y // 50][x // 50]] + old_data[y // 50][
                                                                                                   x // 50 + 1:]
            new_data = open('map_game', 'w')
            for elem in old_data:
                new_data.write(elem)
    else:
        pass


class MyWidget_1(QDialog):
    def __init__(self, tit, ui, par, pos, screen_2, n):
        super().__init__()
        self.setWindowTitle('Give the order my lord')
        uic.loadUi(ui, self)
        self.button_bathe.clicked.connect(lambda: self.bathe(par))
        self.fight_button.clicked.connect(lambda: self.control(pos, screen_2, n, par))
        self.move_button.clicked.connect(lambda: self.move_1(pos, screen_2, n))

    def move_1(self, pos, screen_2, n):
        self.close()
        return go(screen_2, pos, n)

    def control(self, pos, screen_2, n, par):
        self.close()
        return con(screen_2, pos, n, par)

    def bathe(self, n):
        self.close()
        n[3] = ('bathe', 'yes')
        return n


def create_win(tit, ui, par, pos, screen, n):
    app = QApplication(sys.argv)
    application = MyWidget_1('gg', '01.ui', par, pos, screen, n)
    application.show()
    application.move(pos[0] * 50 - 80, pos[1] * 50 + 50)
    app.exec_()
    return par


class Board:

    # создание поля
    def __init__(self, width, height, screen_1):
        self.parametrs = None
        self.screen_1 = screen_1
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 20
        self.top = 20
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        data = open('map_game', 'r').readlines()
        for row in range(self.height):
            for col in range(self.width):
                pygame.draw.rect(screen, 'white', (
                    self.left + self.cell_size * col, self.top + self.cell_size * row, self.cell_size, self.cell_size),
                                 1)
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == '.':
                    img = pygame.image.load('foto/img1.png')
                    screen.blit(img, (j * 50, i * 50))
                elif data[i][j] == '@':
                    img = pygame.image.load('foto/right_plpng.png')
                    screen.blit(img, (j * 50, i * 50))
                elif data[i][j] == '#':
                    img = pygame.image.load('foto/left_pl.png')
                    screen.blit(img, (j * 50, i * 50))
                elif data[i][j] == 'w':
                    img = pygame.image.load('foto/wood_neitral.png')
                    screen.blit(img, (j * 50, i * 50))
                elif data[i][j] == 'd':
                    img = pygame.image.load('foto/wood_left.png')
                    screen.blit(img, (j * 50, i * 50))
                elif data[i][j] == 'D':
                    img = pygame.image.load('foto/wood_right.png')
                    screen.blit(img, (j * 50, i * 50))
                elif data[i][j] == 'i':
                    img = pygame.image.load('foto/iron_n.png')
                    screen.blit(img, (j * 50, i * 50))
                elif data[i][j] == 'm':
                    img = pygame.image.load('foto/iron_left.png')
                    screen.blit(img, (j * 50, i * 50))
                elif data[i][j] == 'M':
                    img = pygame.image.load('foto/iron_right.png')
                    screen.blit(img, (j * 50, i * 50))
                elif data[i][j] == 'g':
                    img = pygame.image.load('foto/gold_n.png')
                    screen.blit(img, (j * 50, i * 50))
                elif data[i][j] == 'z':
                    img = pygame.image.load('foto/gold_l.png')
                    screen.blit(img, (j * 50, i * 50))
                elif data[i][j] == 'Z':
                    img = pygame.image.load('foto/gold_r.png')
                    screen.blit(img, (j * 50, i * 50))
                elif data[i][j] == 'U':
                    img = pygame.image.load('foto/u_l.png')
                    screen.blit(img, (j * 50, i * 50))
                elif data[i][j] == 'u':
                    img = pygame.image.load('foto/u_r.png')
                    screen.blit(img, (j * 50, i * 50))

    def get_click(self, mouse_pos, type_object, n):
        cell = self.get_cell(mouse_pos, type_object, n)
        self.on_click(cell)
        pygame.draw.rect(self.screen_1, 'red', (cell[0] * n, cell[1] * n, n, n), 5)

    def get_cell(self, mouse_pos, n_1, type_object='None_object'):
        x = mouse_pos[0] - self.left
        y = mouse_pos[1] - self.top
        if x < 0 or y < 0:
            return None
        col = x // self.cell_size
        row = y // self.cell_size
        if col >= self.width or row >= self.height:
            return None
        type_object = class_all_objects.Object(col, row, self.screen_1)
        self.parametrs = f'opportunities = {None}'
        old_data = (open('map_game', 'r')).readlines()

        if (col == 0 and row == 0) or (col + 1 == self.width and row + 1 == self.height):
            all_resyrs = [('gold', 0), ('wood', 0), ('iron', 0)]
            self.parametrs = f'hp={100}, opportunities={None}, resurs_players={all_resyrs}'
            type_object = class_Main_building.Main_building(col, row, self.screen_1, self.parametrs)

        elif str(old_data[row])[col] == 'U':
            Player = 'left'
            bathe = 'no'
            self.parametrs = [('hp', 10), ('opportunities', Player), ('dmg', 10), ('bathe', bathe)]
            type_object = class_unit_all.unit(col, row, self.screen_1, self.parametrs)
            create_win('gg', '01.ui', self.parametrs, (col, row), self.screen_1, n_1)

        elif str(old_data[row])[col] == 'u':
            Player = 'right'
            bathe = 'no'
            self.parametrs = [('hp', 10), ('opportunities', Player), ('dmg', 10), ('bathe', bathe)]
            type_object = class_unit_all.unit(col, row, self.screen_1, self.parametrs)
            create_win('gg', '01.ui', self.parametrs, (col, row), self.screen_1, n_1)

        elif (old_data[row][col]) == '.':
            self.parametrs = None
            type_object = clear(col, row, self.screen_1, self.parametrs)


        elif (col != 0 and row != 0) or (col + 1 != self.width and row + 1 != self.height):
            Player = None
            self.parametrs = f'Affiliation_to_player={Player},type_resurs={None}, opportunities={None}'
            old_data = (open('map_game', 'r')).readlines()
            if (old_data[row][col]) == 'g':
                type_object = class_resurs_gold.resurs_gold(col, row, self.screen_1, self.parametrs)
            elif (old_data[row][col]) == 'w':
                type_object = class_resurs_wood.resurs_wood(col, row, self.screen_1, self.parametrs)
            elif (old_data[row][col]) == 'i':
                type_object = class_resurs_iron.resurs_iron(col, row, self.screen_1, self.parametrs)

        return col, row, type_object, self.parametrs

    def on_click(self, cell_coords):
        print(cell_coords)
