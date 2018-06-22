from .constants import DEFAULT_WIDTH, DEFAULT_HEIGHT

from .figures import Figure


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

        self.board = [[0 for dummy_w in range(self.width)] for dummy_h in range(self.height)]
        self.state = True

        self.figure = Figure(Figure.get_random())
        self.starting_position = [int(self.width / 2) - int(self.figure.get_sprite_size() / 2),
                                  -self.figure.get_sprite_size()]
        self.figure_position = self.get_starting_position()

    def __str__(self):
        return '\n'.join(str(x) for x in self.board)

    def is_available(self, x, y):
        if self.width > x >= 0 and self.height > y:
            return self.board[y][x] == 0
        else:
            # Index out of range
            return False

    def get_pixel_size(self):
        """ Return board size in pixels """
        return self.pixel_size

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
                        p_idx * self.pixel_ratio,
                        l_idx * self.pixel_ratio,
                        self.pixel_ratio,
                        self.pixel_ratio
                    ))
        return arr

    def repr_figure_on_board(self):
        """ Represents figure coordinates on board """
        arr = []
        for l_idx, line in enumerate(self.figure.get_state()):
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
                pos[0] * self.pixel_ratio,
                pos[1] * self.pixel_ratio,
                self.pixel_ratio,
                self.pixel_ratio
            ]
            for pos in self.repr_figure_on_board()
        ]

    def move_figure(self):
        """ Moving figure bottom """
        if self.check_bottom():
            self.figure_position[1] += 1

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

    def check_collision(self):
        """ Check collisions of figure object on board """
        self.check_left()

    def check_left(self):
        """ check left collisions """
        for block in self.repr_figure_on_board():
            print(block[0])
            if not self.is_available(block[0] - 1, block[1]):
                return False
        return True

    def check_right(self):
        """ Check right collision """
        for block in list(self.repr_figure_on_board()):
            if not self.is_available(block[0], block[1] + 1):
                return False
        return True

    def check_bottom(self):
        """ Check bottom colision """
        for block in list(self.repr_figure_on_board()):
            if not self.is_available(block[0], block[1]+1):
                return False
        return True
