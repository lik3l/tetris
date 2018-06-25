import time
from pygame import locals as c


def input_handler(pygame, board):
    pressed = pygame.key.get_pressed()
    if pressed[c.K_LEFT]:
        board.figure_left()
        pygame.display.flip()
        time.sleep(.12)
    if pressed[c.K_RIGHT]:
        board.figure_right()
        pygame.display.flip()
        time.sleep(.12)
    if pressed[c.K_DOWN]:
        board.speed_down()
        pygame.display.flip()
        time.sleep(.05)
    if pressed[c.K_SPACE]:
        board.rotate_right()
        pygame.display.flip()
        time.sleep(.15)
    if pressed[c.K_LALT]:
        board.rotate_left()
        pygame.display.flip()
        time.sleep(.15)
