import sys

from PyQt5.QtWidgets import QApplication
from const import *
from start_screen import start_screen

import class_Main_building
import class_random_resurs_in_map
import class_resurs_gold
import class_unit_all
from class_unit_all import *
from unit_window import *
from unit_window import *

global screen


def create_win(tit, ui, par, pos):
    app = QApplication(sys.argv)
    application = MyWidget_1('gg', '01.ui', par, pos)
    application.show()
    app.exec_()
    return par


def terminate():
    pygame.quit()
    sys.exit()


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

    def get_click(self, mouse_pos, type_object, n):
        cell = self.get_cell(mouse_pos, type_object)
        self.on_click(cell)
        pygame.draw.rect(self.screen_1, 'red', (cell[0] * n, cell[1] * n, n, n), 5)

    def get_cell(self, mouse_pos, type_object='None_object'):
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
            create_win('gg', '01.ui', self.parametrs, (col, row))

        elif (old_data[row][col]) == '.':
            self.parametrs = None
            type_object = class_random_resurs_in_map.resurs(col, row, self.screen_1, self.parametrs)


        elif (col != 0 and row != 0) or (col + 1 != self.width and row + 1 != self.height):
            Player = None
            self.parametrs = f'Affiliation_to_player={Player},type_resurs={None}, opportunities={None}'
            old_data = (open('map_game', 'r')).readlines()
            if (old_data[row][col]) == 'g':
                type_object = class_resurs_gold.resurs_gold(col, row, self.screen_1, self.parametrs)
            elif (old_data[row][col]) == 'w':
                type_object = class_resurs_gold.resurs_gold(col, row, self.screen_1, self.parametrs)
            elif (old_data[row][col]) == 'i':
                type_object = class_resurs_gold.resurs_gold(col, row, self.screen_1, self.parametrs)

        print(old_data)
        return col, row, type_object, self.parametrs

    def on_click(self, cell_coords):
        print(cell_coords)


if __name__ == '__main__':
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    if start_screen(screen):
        terminate()
    pygame.quit()
