from .constants import DEFAULT_WIDTH, DEFAULT_HEIGHT

from .figures import Figure
from .score import Score


class Board:
    """
    Base board class used to represent game board
    """
    def __init__(self, width, height):
        self.screen_ratio = width / height
        if self.screen_ratio >= 0.5:
            # Calc through width
            self.pixel_ratio = int(height / DEFAULT_HEIGHT)
        else:
            # calc through height
            self.pixel_ratio = int(width / DEFAULT_WIDTH)
        self.width = DEFAULT_WIDTH
        self.height = DEFAULT_HEIGHT
        self.pixel_size = (self.width * self.pixel_ratio,
                           self.height * self.pixel_ratio)
        self.board = [[]]
        self._set_board()
        self.state = False

        self.figure = Figure(Figure.get_random())
        self.starting_position = (int(self.width / 2) - int(self.figure.get_sprite_size() / 2),
                                  -self.figure.get_sprite_size())
        self.figure_position = self.get_starting_position()

        self.score = Score()
        self.score_state = False
        self.end_game_state = True

    def __str__(self):
        return '\n'.join(str(x) for x in self.board)

    def reset_board(self):
        """ Reset board on restart """
        self._set_board()
        self.state = True
        self.end_game_state = False
        self.score_state = False
        self.figure = Figure(Figure.get_random())
        self.figure_position = self.get_starting_position()
        self.score = Score()

    def _set_board(self):
        self.board = [[0 for dummy_w in range(self.width)] for dummy_h in range(self.height)]

    def get_game_state(self):
        """ Returns True if game is running """
        return self.state

    def is_available(self, x, y):
        if self.width > x >= 0 and self.height > y >= 0:
            return self.board[y][x] == 0
        elif y < 0 <= x < self.width:
            return True
        else:
            # Index out of range
            return False

    def check_figure(self, figure):
        """ Checks figure aviability """
        for coords in figure:
            if not self.is_available(*coords):
                return False
        return True

    def get_fullness(self):
        """ Returns percentage of board fullness """
        for idx, line in enumerate(self.board):
            if any(line):
                return 1 - idx / self.height

    def rotate_right(self):
        """ Checks and rotates figure """
        if self.check_rotate('right'):
            self.figure.rotate_right()

    def rotate_left(self):
        """ Checks and rotates figure """
        if self.check_rotate('left'):
            self.figure.rotate_left()

    def set_board_position(self, x, y):
        """ Sets block in position as used """
        try:
            self.board[y][x] = 1
        except IndexError:
            print(self)
            print(self.repr_figure_on_board())
            print(x, y)
            # TODO: Catch error

    def get_pixel_size(self):
        """ Return board size in pixels """
        return self.pixel_size

    def get_block_size(self):
        return self.pixel_ratio, self.pixel_ratio

    def make_random_figure(self):
        """ Makes random figure """
        self.figure = Figure(Figure.get_random())
        self.figure_position = self.get_starting_position()

    def get_starting_position(self):
        """ Returns starting pos """
        return list(self.starting_position)

    def print_board(self):
        """ Returns represented board coords """
        arr = []
        for l_idx, line in enumerate(self.board):
            for p_idx, pixel in enumerate(line):
                if pixel:
                    arr.append((
                        p_idx * self.pixel_ratio - 1,
                        l_idx * self.pixel_ratio + 1,
                        self.pixel_ratio - 1,
                        self.pixel_ratio - 1
                    ))
        return arr

    def repr_figure_on_board(self, **kwargs):
        """ Represents figure coordinates on board """
        figure = self.figure.get_state()
        if kwargs.get('figure'):
            figure = kwargs['figure']
        arr = []
        for l_idx, line in enumerate(figure):
            for p_idx, pixel in enumerate(line):
                if pixel:
                    arr.append([
                        self.figure_position[0] + p_idx,
                        self.figure_position[1] + l_idx
                    ])
        return arr

    def print_figure(self):
        """ Return represented figure coords """
        return [
            [
                pos[0] * self.pixel_ratio - 1,
                pos[1] * self.pixel_ratio + 1,
                self.pixel_ratio - 1,
                self.pixel_ratio - 1
            ]
            for pos in self.repr_figure_on_board()
        ]

    def move_figure(self):
        """ Moving figure bottom """
        if self.check_bottom():
            self.figure_position[1] += 1
            return True
        else:
            return False

    def speed_down(self):
        """ Speeds figure down """
        if self.check_bottom():
            self.figure_position[1] += 1

    def figure_left(self):
        """ Moves figure to the left """
        if self.check_left():
            self.figure_position[0] -= 1

    def figure_right(self):
        """ Moves figure to the right """
        if self.check_right():
            self.figure_position[0] += 1

    def check_left(self):
        """ check left collisions """
        for block in self.repr_figure_on_board():
            if not self.is_available(block[0] - 1, block[1]):
                return False
        return True

    def check_right(self):
        """ Check right collision """
        for block in list(self.repr_figure_on_board()):
            if not self.is_available(block[0] + 1, block[1]):
                return False
        return True

    def check_bottom(self):
        """ Check bottom collision """
        for block in list(self.repr_figure_on_board()):
            if not self.is_available(block[0], block[1]+1):
                self.stack_figure()
                return False
        return True

    def check_rotate(self, path):
        """ Check rotate availability """
        if path == 'left':
            repr_fig = self.repr_figure_on_board(
                figure=self.figure.get_next_left()
            )
            return self.check_figure(repr_fig)
        else:
            repr_fig = self.repr_figure_on_board(
                figure=self.figure.get_next_right()
            )
            return self.check_figure(repr_fig)

    def stack_figure(self):
        """ Stacks figure on board """
        for coords in self.repr_figure_on_board():
            self.set_board_position(*coords)
        self.remove_lines(self.get_full())
        if self.check_endgame():
            self.end_game()
            self.set_score_state()
            return
        self.make_random_figure()

    def get_full(self):
        """ Returns full board line ids """
        return [idx for idx, line in enumerate(self.board) if all(line)]

    def remove_lines(self, lines):
        """ Remove lines by line id """
        for line_idx in lines:
            self.board.pop(line_idx)
            self.board.insert(0, [0] * self.width)
        self.score.increase_score(len(lines))

    def check_endgame(self):
        """ Returns True if game over """
        return any(self.board[0])

    def get_score_state(self):
        """ Represents score writing """
        return self.score_state

    def set_score_state(self):
        self.score_state = True

    def end_score_state(self):
        self.score_state = False

    def end_game(self):
        self.state = False

    def get_end_game_state(self):
        return self.end_game_state

    def set_end_game(self):
        self.end_game_state = True
