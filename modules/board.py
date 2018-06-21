class Board:
    """
    Base board class used to represent game board
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for dummy_w in range(width)] for dummy_h in range(height)]

    def __str__(self):
        return '\n'.join(str(x) for x in self.board)

    def is_available(self, x, y):
        return self.board[x][y] == 0
