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


class KeyMap:
    LEFT = (c.K_LEFT, c.K_a)
    RIGHT = (c.K_RIGHT, c.K_d)
    DOWN = c.K_DOWN, c.K_s
    R_RIGHT = c.K_SPACE, c.K_e
    R_LEFT = c.K_LEFT, c.K_q
    KEYS = [LEFT, RIGHT, DOWN, R_RIGHT, R_LEFT]
    ACTIONS = const.MOVE_ACTIONS

    def __init__(self):
        self.keys = [k[0] for k in self.KEYS]
        self.key_hold = set()

    def get_keys(self):
        return self.keys

    def get_preseed(self):
        return self.key_hold

    def get_action(self, key):
        for k, action in zip(self.keys, self.ACTIONS):
            if k == key:
                return action

    def press_key(self, key):
        self.key_hold.add(key)

    def leave_key(self, key):
        self.key_hold.remove(key)


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


def end_game_state_handler(event, game):
    if event.type == game.pygame.QUIT:
        sys.exit()
    elif event.type == game.pygame.KEYDOWN:
        if event.key == game.pygame.K_UP:
            game.end_game.move_up()
        elif event.key == game.pygame.K_DOWN:
            game.end_game.move_down()
        elif event.key == game.pygame.K_RETURN:
            game.up_down()
            game.end_game.submit(game)
