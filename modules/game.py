class Game:
    GAME_STATE = 0
    SCORE_STATE = 2
    ENDGAME_STATE = 3

    def __init__(self, board, pygame, screen):
        self.board = board
        self.pygame = pygame
        self.screen = screen
        self.pause_state = False

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
