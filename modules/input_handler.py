import sys

from pygame import locals as c
from modules import constants as const


class KeyMap:
    LEFT = (c.K_LEFT, c.K_a)
    RIGHT = (c.K_RIGHT, c.K_d)
    DOWN = c.K_DOWN, c.K_s
    R_RIGHT = c.K_SPACE, c.K_e
    R_LEFT = c.K_LEFT, c.K_q
    # do not modify order
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

    def clear_pressed(self):
        self.key_hold = set()

    def press_key(self, key):
        self.key_hold.add(key)

    def leave_key(self, key):
        self.key_hold.remove(key)


def end_game_state_handler(event, game):
    if event.type == game.pygame.QUIT:
        sys.exit()
    elif event.type == game.pygame.KEYDOWN:
        if event.key == game.pygame.K_UP:
            game.menu.move_up()
        elif event.key == game.pygame.K_DOWN:
            game.menu.move_down()
        elif event.key == game.pygame.K_RETURN:
            game.clear_input()
            game.menu.submit(game)
