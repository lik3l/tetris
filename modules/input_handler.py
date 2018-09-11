import sys

from pygame import locals as c
from modules import constants as const


def left(board):
    board.figure_left()


def right(board):
    board.figure_right()


def s_down(board):
    board.speed_down()


def r_right(board):
    board.rotate_right()


def r_left(board):
    board.rotate_left()


pressed_keys_map = {
    c.K_LEFT: {'count': 0, 'action': left, 'wait': True},
    c.K_RIGHT: {'count': 0, 'action': right, 'wait': True},
    c.K_DOWN: {'count': 0, 'action': s_down, 'wait': False},
    c.K_SPACE: {'count': 0, 'action': r_right, 'wait': True},
    c.K_LALT: {'count': 0, 'action': r_left, 'wait': True},
}


def input_handler(pygame, board):
    pressed = pygame.key.get_pressed()
    for k in pressed_keys_map:
        if pressed[k]:
            if pressed_keys_map[k]['count'] > 1 \
                    or not pressed_keys_map[k]['count']:
                pressed_keys_map[k]['action'](board)
                pygame.display.flip()
            pressed_keys_map[k]['count'] += 1


def input_up_handler(pygame, speed):
    pressed = pygame.key.get_pressed()
    for k in pressed_keys_map:
        if not pressed[k]:
            if k == pygame.K_DOWN:
                pygame.time.set_timer(const.MOVEDOWN, speed)
            pressed_keys_map[k]['count'] = 0


def end_game_state_handler(end_game, event, pygame, reset):
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            end_game.move_up()
        elif event.key == pygame.K_DOWN:
            end_game.move_down()
        elif event.key == pygame.K_RETURN:
            end_game.submit(reset)
