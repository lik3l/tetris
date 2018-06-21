from .constants import DEFAULT_WIDTH, DEFAULT_HEIGHT


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
        self.pixel_size = (width, height)
        self.width = DEFAULT_WIDTH
        self.height = DEFAULT_HEIGHT
        self.board = [[0 for dummy_w in range(self.width)] for dummy_h in range(self.height)]

    def __str__(self):
        return '\n'.join(str(x) for x in self.board)

    def is_available(self, x, y):
        return self.board[x][y] == 0
