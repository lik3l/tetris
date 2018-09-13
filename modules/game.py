from modules import constants as c
from modules.flow_handlers import game_flow_handler, score_flow_handler
from modules.helpers import draw_rect, get_board_color, write_end_text, get_not_scored, enter_player_name
from modules.input_handler import end_game_state_handler, KeyMap


class Game:
    GAME_STATE = 0
    SCORE_STATE = 2
    ENDGAME_STATE = 3

    def __init__(self, board, pygame, screen, end_game, block_bg, myfont):
        self.board = board
        self.pygame = pygame
        self.screen = screen
        self.board_rect = pygame.Rect((self.screen.get_size()[0] // 2 - board.get_pixel_size()[0] // 2,
                                       0, *board.get_pixel_size()))
        self.board_surf = self.screen.subsurface(self.board_rect)
        self.end_game = end_game
        self.pause_state = False
        self.default_speed = c.DEFAULT_SPEED
        self.speed = self.default_speed
        self.round = 1
        self.block_bg = block_bg
        self.font = myfont
        self.keymap = KeyMap()

    def get_state(self):
        if self.board.get_game_state():
            return self.GAME_STATE
        elif self.board.get_end_game_state():
            return self.ENDGAME_STATE
        elif self.board.get_score_state():
            return self.SCORE_STATE

    def get_board(self):
        return self.board_surf

    def pause(self):
        self.pause_state = not self.pause_state

    def is_paused(self):
        return self.pause_state

    def key_down(self, key):
        if key in self.keymap.get_keys():
            self.do_action(self.keymap.get_action(key))

    def key_up(self):
        pass

    def is_holding(self):
        return False

    def do_action(self, action):
        if action == c.LEFT:
            self._move_left()
        elif action == c.RIGHT:
            self._move_right()
        elif action == c.DOWN:
            self._move_down()
        elif action == c.R_RIGHT:
            self._rotate_right()
        elif action == c.R_LEFT:
            self._rotate_left()

    def _move_left(self):
        self.board.figure_left()

    def _move_right(self):
        self.board.figure_right()

    def _move_down(self):
        self.board.speed_down()

    def _rotate_left(self):
        self.board.rotate_left()

    def _rotate_right(self):
        self.board.rotate_right()

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def set_default_speed(self):
        self.speed = self.default_speed

    def next_round(self):
        self.round += 1
        self.speed = int(self.speed * 0.9)
        self.pygame.time.set_timer(c.MOVEDOWN, self.speed)

    def get_round(self):
        return self.round

    def init_timer(self):
        self.pygame.time.set_timer(c.MOVEDOWN, self.speed)

    def _gameplay_flow(self):
        """ Game running state """
        for event in self.pygame.event.get():
            game_flow_handler(event, self)

        if not self.is_paused():
            self.board_surf.fill(c.BLACK)
            for coords in self.board.print_board():
                draw_rect(self.board_surf, get_board_color(self.board.get_fullness()), coords, self.block_bg)
            for coords in self.board.print_figure():
                draw_rect(self.board_surf, self.board.figure.get_color(), coords, self.block_bg)
        else:
            write_end_text(self.screen, [self.font.render('Paused', 1, c.WHITE)], self.screen.get_size())

        scoretext = self.font.render(self.board.score.get_score(), 1, c.WHITE)
        self.board_surf.blit(scoretext, (5, 10))
        if self.board.score.get_int_score() >= 100 * self.get_round():
            self.next_round()
        self.pygame.display.flip()

    def _score_flow(self):
        """ Show and input score """
        self.screen.fill(c.BLACK)

        if not self.board.score.check_score():
            text = get_not_scored(self.font, self.board, c.WHITE)
        else:
            text = enter_player_name(self.font, self.board, c.WHITE)
        write_end_text(self.screen, text, self.screen.get_size())

        for event in self.pygame.event.get():
            score_flow_handler(event, self)

        self.pygame.display.flip()

    def _menu_flow(self):
        self.screen.fill(c.BLACK)

        self.end_game.draw()
        for event in self.pygame.event.get():
            end_game_state_handler(event, self)
        self.pygame.display.flip()

    def flow(self):
        if self.get_state() == self.GAME_STATE:
            self._gameplay_flow()
        elif self.get_state() == self.SCORE_STATE:
            self._score_flow()
        elif self.get_state() == self.ENDGAME_STATE:
            self._menu_flow()

    def reset(self):
        self.screen.fill(c.GRAY)
        self.board.reset_board()
        self.set_default_speed()
        self.round = 1
        self.pygame.time.set_timer(c.MOVEDOWN, self.speed)
