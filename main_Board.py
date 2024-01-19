from Board_in_game import *
from helpper_program import drow_map
from start_screen import start_screen
import os


def terminate():
    pygame.quit()
    sys.exit()


x = 220
y = 20
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
pygame.init()
pygame.display.set_caption('KING_FIGHT')
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
n = 50
if start_screen(screen):
    terminate()
size = width, height = 1500, 1000
screen = pygame.display.set_mode(size)
board = Board(int(width / n), int(height / n), screen)
board.set_view(0, 0, n)


def start():
    if __name__ == '__main__':
        # здесь сорокет заменить вводом переменной в игровх настройках
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill((0, 0, 0))
                    board.get_click(event.pos, None, n)
                    board.render(screen)
            # screen.fill((0, 0, 0))
            board.render(screen)
            pygame.display.flip()
        pygame.quit()


drow_map()
start()
