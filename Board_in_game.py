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

i = 1


def go(sc, pos, n, flag):
    if flag:
        old_data = (open('map_game', 'r')).readlines()
        x, y = pygame.mouse.get_pos()
        if ((old_data[y // 50]).split()[x // 50]) == '.' and (pos[0] + 2 >= x // 50 >= pos[0] - 2) and (
                pos[1] + 2 >= y // 50 >= pos[1] - 2):
            f = old_data[y // 50].split()
            f[x // 50] = old_data[pos[1]].split()[pos[0]]
            old_data[y // 50] = ' '.join(f) + '\n'
            f = (old_data[pos[1]]).split()
            f[pos[0]] = '. '
            old_data[pos[1]] = ' '.join(f) + '\n'
            new_data = open('map_game', 'w')
            for elem in old_data:
                new_data.write(elem)
    else:
        old_data = (open('map_game', 'r')).readlines()
        new_data = open('map_game', 'w')
        for elem in old_data:
            new_data.write(elem)


def control(pos, par, sc, n):
    A = {'M': 'm', 'i': 'm', 'g': 'z', 'Z': 'z', 'w': 'd', 'D': 'd'}
    B = {'m': 'M', 'i': 'M', 'g': 'Z', 'z': 'Z', 'w': 'D', 'd': 'D'}
    old_data = (open('map_game', 'r')).readlines()
    x, y = pygame.mouse.get_pos()
    if (old_data[y // 50].split()[x // 50]) != '.' and (old_data[y // 50].split()[x // 50]) != '#' and (
            old_data[y // 50].split()[x // 50]) != '@' and (old_data[y // 50].split()[x // 50]) != 'U' and (
            old_data[y // 50].split()[x // 50]) != 'u' and (old_data[y // 50].split()[x // 50]) != '.' and (
            pos[0] + 2 >= x // 50 >= pos[0] - 2) and (
            pos[1] + 2 >= y // 50 >= pos[1] - 2):

        if par[1][1] == 'left' and (  # тут
                old_data[y // 50].split()[x // 50]) != 'd' and (old_data[y // 50].split()[x // 50]) != 'z' and (
                old_data[y // 50].split()[x // 50]) != 'm':

            f = old_data[y // 50].split()
            f[x // 50] = A[old_data[y // 50].split()[x // 50]]
            old_data[y // 50] = ' '.join(f) + '\n'



        elif par[1][1] == 'right' and (
                old_data[y // 50][x // 50]) != 'D' and (old_data[y // 50][x // 50]) != 'Z' and (
                old_data[y // 50][x // 50]) != 'M':  # тут
            f = old_data[y // 50].split()
            f[x // 50] = B[old_data[y // 50].split()[x // 50]]
            old_data[y // 50] = ' '.join(f) + '\n'

        new_data = open('map_game', 'w')
        for elem in old_data:
            new_data.write(elem)
    else:
        pass


def fight(pos, par, sc, n):
    old_data = (open('map_game', 'r')).readlines()
    x, y = pygame.mouse.get_pos()
    if par[1][1] == 'left' and old_data[y // 50].split()[x // 50][0] == 'u':
        if old_data[y // 50].split()[x // 50][2:4] == '10':
            f = old_data[y // 50].split()
            f[x // 50] = 'u[5,5]'
            old_data[y // 50] = ' '.join(f) + '\n'
        else:
            f = old_data[y // 50].split()
            f[x // 50] = '.'
            old_data[y // 50] = ' '.join(f) + '\n'
    if par[1][1] == 'right' and old_data[y // 50].split()[x // 50][0] == 'U':
        if old_data[y // 50].split()[x // 50][2:4] == '10':
            f = old_data[y // 50].split()
            f[x // 50] = 'U[5,5]'
            old_data[y // 50] = ' '.join(f) + '\n'
        elif old_data[y // 50].split()[x // 50][2:4] == '5,':
            f = old_data[y // 50].split()
            f[x // 50] = '.'
            old_data[y // 50] = ' '.join(f) + '\n'
    if par[1][1] == 'right' and old_data[y // 50].split()[x // 50][0] == '#':
        n_d = int(old_data[y // 50][old_data[y // 50].index(',') + 1:old_data[y // 50].index(']')]) - 5
        k = (old_data[0].split()[0][old_data[0].split()[0].index(',') + 1:old_data[0].split()[0].index(']')])
        f = old_data[0]
        if (int(f[f.index(',') + 1:f.index(']')])) == 0:
            print('red win')
            exit()
        f = ''.join(f.replace(k, str(n_d), 1))
        old_data[y // 50] = f
    if par[1][1] == 'left' and old_data[y // 50].split()[x // 50][0] == '@':
        f = old_data[y // 50].split()[x // 50]
        f = f.replace(f[f.index(',') + 1:f.index(']')], str(int(f[f.index(',') + 1:f.index(']')]) - 5))
        if (int(f[f.index(',') + 1:f.index(']')])) == 0:
            print('blue win')
            exit()  # сделать окно победы
        f_1 = old_data[y // 50].replace(old_data[y // 50].split()[x // 50], f, 1)
        old_data[y // 50] = f_1

    new_data = open('map_game', 'w')
    for elem in old_data:
        new_data.write(elem)


class MyWidget_1(QDialog):
    def __init__(self, tit, ui, par, pos, screen_2, n):
        super().__init__()
        self.setWindowTitle('Give the order my lord')
        uic.loadUi(ui, self)
        self.button_fight.clicked.connect(lambda: self.fight(pos, par, screen_2, n))
        self.fight_button.clicked.connect(lambda: self.control(pos, par, screen_2, n))
        self.move_button.clicked.connect(lambda: self.move_1(par, pos, screen_2, n))

    def move_1(self, par, pos, screen_2, n):
        self.close()
        global i
        if (i % 2 != 0) and (par[1][1] == 'left'):
            flag = True
            i += 1
            return go(screen_2, pos, n, flag)
        elif (i % 2 == 0) and (par[1][1] == 'right'):
            flag = True
            i += 1
            return go(screen_2, pos, n, flag)
        else:
            flag = False
            return go(screen_2, pos, n, flag)

    def control(self, pos, par, screen_2, n):
        self.close()
        # print(par)
        return control(pos, par, screen_2, n)

    def fight(self, pos, par, screen_2, n):
        self.close()
        return fight(pos, par, screen_2, n)


def create_win(tit, ui, par, pos, screen, n):
    app = QApplication(sys.argv)
    application = MyWidget_1('gg', '01.ui', par, pos, screen, n)
    application.show()
    app.exec_()
    return par


class win_build(QDialog):
    def __init__(self, tit, ui, par, pos, screen_2, n):
        super().__init__()
        self.setWindowTitle('Give the order my lord')
        uic.loadUi(ui, self)
        self.pushButton_gen_gold.clicked.connect(lambda: self.create_for_gold(pos, par, screen_2, n))
        self.pushButton_gen_iron_wood.clicked.connect(lambda: self.create_for_iron_and_wood(pos, par, screen_2))

    def create_for_gold(self, pos, par, screen_2, n):
        self.close()
        old_data = (open('map_game', 'r')).readlines()
        f = old_data[pos[1]].split()[pos[0]]
        k = (f[f.index("d',") + 3:f.index(')')])
        k_1 = k.replace(f[f.index("d',") + 3:f.index(')')], str(int(f[f.index("d',") + 3:f.index(')')])))
        if par[1][1] == 'left' and int(k) >= 5:  # тут
            old_data[0] = old_data[0].replace('.', 'U[10,5]', 1)  # тут
            f = old_data[0].split()[0]
            f = f.replace(str(int(k_1)), str(int(k_1) - 5), 1)
            old_data[0] = old_data[0].replace(str(old_data[0].split()[0]), f, 1)
        elif par[1][1] == 'right' and int(k) >= 5:
            old_data[19] = old_data[19][::-1].replace('.', 'u', 1)[::-1]  # тут
            old_data[19] = old_data[19].replace('u', 'u[10,5]', 1)
            f = old_data[19].split()[29]
            k = (f[f.index("d',") + 3:f.index(')')])
            k_1 = k.replace(f[f.index("d',") + 3:f.index(')')], str(int(f[f.index("d',") + 3:f.index(')')])))
            f = f.replace("d'," + str(int(k_1)), "d'," + str(int(k_1) - 5), 1)
            old_data[19] = old_data[19].replace(str(old_data[19].split()[29]), f, 1)
        new_data = open('map_game', 'w')
        for elem in old_data:
            new_data.write(elem)
        return par

    def create_for_iron_and_wood(self, pos, par, screen):
        self.close()
        old_data = (open('map_game', 'r')).readlines()
        f = old_data[pos[1]].split()[pos[0]]
        w_r, i_r = (f[f.index("od',"):f.index(("),('i"))], f[f.index("n',"):f.index(")]")])
        i_w_r, i_i_r = int(w_r[4:]), int(i_r[3:])
        f = f.replace(w_r, "od'," + str(i_w_r - 5))
        f = f.replace(i_r, "n'," + str(i_i_r - 5))
        f_1 = old_data[pos[1]].split()
        f_1[pos[0]] = f
        f_1 = ' '.join(f_1)
        if i_w_r >= 5 and i_i_r >= 5:
            old_data[pos[1]] = f_1 + '\n'
            if par[1][1] == 'left':  # тут
                old_data[0] = old_data[0].replace('.', 'U[10,5]', 1)  # тут
            else:
                old_data[19] = old_data[19][::-1].replace('.', 'u', 1)[::-1]  # тут
                old_data[19] = old_data[19].replace('u', 'u[10,5]', 1)
        new_data = open('map_game', 'w')
        for elem in old_data:
            new_data.write(elem)
        self.close()


def create_win_build(tit, ui, par, pos, screen, n):
    app = QApplication(sys.argv)
    win = win_build('gg', '02.ui', par, pos, screen, n)
    win.show()
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
        for row in range(self.height):
            for col in range(self.width):
                pygame.draw.rect(screen, 'white', (
                    self.left + self.cell_size * col, self.top + self.cell_size * row, self.cell_size, self.cell_size),
                                 1)

        elements = {'.': pygame.image.load('foto/img1.png'),
                    '@': pygame.image.load('foto/right_plpng.png'),
                    '#': pygame.image.load('foto/left_pl.png'),
                    'w': pygame.image.load('foto/wood_neitral.png'),
                    'd': pygame.image.load('foto/wood_left.png'),
                    'D': pygame.image.load('foto/wood_right.png'),
                    'i': pygame.image.load('foto/iron_n.png'),
                    'm': pygame.image.load('foto/iron_left.png'),
                    'M': pygame.image.load('foto/iron_right.png'),
                    'g': pygame.image.load('foto/gold_n.png'),
                    'z': pygame.image.load('foto/gold_l.png'),
                    'Z': pygame.image.load('foto/gold_r.png'),
                    'U': pygame.image.load('foto/u_l.png'),
                    'u': pygame.image.load('foto/u_r.png')}
        data = open('map_game', 'r').readlines()
        for i in range(len(data)):
            for j in range(len((data[i]).split())):
                screen.blit(elements[(data[i]).split()[j][0]], (j * 50, i * 50))

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
            self.parametrs = [['hp', 100], ['opportunities', '....'], ['resurs_players', all_resyrs]]
            type_object = class_Main_building.Main_building(col, row, self.screen_1, self.parametrs)
            if col == 0:
                self.parametrs[1][1] = 'left'
            else:
                self.parametrs[1][1] = 'right'
            create_win_build('gg', '02.ui', self.parametrs, (col, row), self.screen_1, n_1)

        elif str(old_data[row]).split()[col][0] == 'U' or str(old_data[row]).split()[col][0] == 'u':
            if str(old_data[row]).split()[col][0] == 'U':
                Player = 'left'
            else:
                Player = 'right'
            bathe = 'no'
            self.parametrs = [('hp', 10), ('opportunities', Player), ('dmg', 10), ('motion', 1)]
            type_object = class_unit_all.unit(col, row, self.screen_1, self.parametrs)
            if self.parametrs[1][1] == 'left':
                self.parametrs = [('hp', 10), ('opportunities', Player), ('dmg', 10)]
            elif self.parametrs[1][1] == 'right':
                self.parametrs = [('hp', 10), ('opportunities', Player), ('dmg', 10)]
            create_win('gg', '01.ui', self.parametrs, (col, row), self.screen_1, n_1)



        elif ((old_data[row]).split()[col]) == '.':
            self.parametrs = None
            type_object = clear(col, row, self.screen_1, self.parametrs)


        elif (col != 0 and row != 0) or (col + 1 != self.width and row + 1 != self.height):
            Player = None
            self.parametrs = f'Affiliation_to_player={Player},type_resurs={None}, opportunities={None}'
            old_data = (open('map_game', 'r')).readlines()
            if ((old_data[row]).split()[col]) == 'g':
                type_object = class_resurs_gold.resurs_gold(col, row, self.screen_1, self.parametrs)
            elif ((old_data[row]).split()[col]) == 'w':
                type_object = class_resurs_wood.resurs_wood(col, row, self.screen_1, self.parametrs)
            elif ((old_data[row]).split()[col]) == 'i':
                type_object = class_resurs_iron.resurs_iron(col, row, self.screen_1, self.parametrs)

        return col, row, type_object, self.parametrs

    def on_click(self, cell_coords):
        pass
        # print(cell_coords)
