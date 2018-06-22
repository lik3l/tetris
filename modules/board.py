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
        self.starting_position = [int(self.width / 2) - 2, 0]

        self.board = [[0 for dummy_w in range(self.width)] for dummy_h in range(self.height)]
        self.state = True
        self.figure = Figure(Figure.get_random())
        self.figure_position = list(self.starting_position)

    def __str__(self):
        return '\n'.join(str(x) for x in self.board)

    def is_available(self, x, y):
        return self.board[x][y] == 0

    def get_pixel_size(self):
        """ Return board size in pixels """
        return self.pixel_size

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

    def print_figure(self):
        """ Return represented figure coords """
        arr = []
        for l_idx, line in enumerate(self.figure.get_state()):
            for p_idx, pixel in enumerate(line):
                if pixel:
                    arr.append((
                        (self.figure_position[0] + p_idx) * self.pixel_ratio,
                        (self.figure_position[1] + l_idx) * self.pixel_ratio,
                        self.pixel_ratio, self.pixel_ratio
                    ))
        return arr

    def move_figure(self):
        """ Moving figure bottom """
        self.figure_position[1] += 1


