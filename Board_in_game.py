import pygame

import class_Main_building
import class_all_objects
import class_random_resurs_in_map


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

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

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
        if (col == 0 and row == 0) or (col + 1 == self.width and row + 1 == self.height):
            self.parametrs = f'hp={100}, opportunities={None}'
            type_object = class_Main_building.Main_building(col, row, self.screen_1, self.parametrs)
        elif 15 > col > 4 and 15 > row > 5:
            Player = None
            self.parametrs = f'Affiliation_to_player={Player},type_resurs={None}, opportunities={None}'
            type_object = class_random_resurs_in_map.resurs(col, row, self.screen_1, self.parametrs)
        return (col, row, type_object, self.parametrs)

    def on_click(self, cell_coords):
        print(cell_coords)
