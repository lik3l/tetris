class Game:
    GAME_STATE = 0
    SCORE_STATE = 2
    ENDGAME_STATE = 3

    def __init__(self, board, pygame, screen):
        self.board = board
        self.pygame = pygame
        self.screen = screen
        self.state = self.GAME_STATE
        self.pause_state = False

    def get_state(self):
        return self.state

    def pause(self):
        self.pause_state = not self.pause_state

    def is_paused(self):
        return self.pause_state
