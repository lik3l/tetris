from modules import constants as c


class Game:
    GAME_STATE = 0
    SCORE_STATE = 2
    ENDGAME_STATE = 3

    def __init__(self, board, pygame, screen, end_game):
        self.board = board
        self.pygame = pygame
        self.screen = screen
        self.end_game = end_game
        self.pause_state = False
        self.default_speed = c.DEFAULT_SPEED
        self.speed = self.default_speed
        # Needed to break keypress repeat
        self.k_down_pressed = False

    def get_state(self):
        if self.board.get_game_state():
            return self.GAME_STATE
        elif self.board.get_end_game_state():
            return self.ENDGAME_STATE
        elif self.board.get_score_state():
            return self.SCORE_STATE

    def pause(self):
        self.pause_state = not self.pause_state

    def is_paused(self):
        return self.pause_state

    def press_down(self):
        self.k_down_pressed = True

    def up_down(self):
        self.k_down_pressed = False

    def pressed_down(self):
        return self.k_down_pressed

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def set_default_speed(self):
        self.speed = self.default_speed
