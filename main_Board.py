import pygame
from Board_in_game import Board

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)
    board = Board(int(width/40), int(height/40), screen)
    board.set_view(0, 0, 40)
    #здесь сорокет заменить вводом переменной в игровх настройках
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
