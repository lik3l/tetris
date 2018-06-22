import time
from pygame import locals as c


def input_handler(pygame, board):
    pressed = pygame.key.get_pressed()
    if pressed[c.K_LEFT]:
        board.figure_left()
        
        time.sleep(.4)
        print('left')
    if pressed[c.K_RIGHT]:
        print('right')