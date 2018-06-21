from .constants import FIGURE_FORMS


class Figure:
    """
    Base figure model used to describe figure and it's moves
    """
    def __init__(self, figure):
        self.figure = FIGURE_FORMS[figure]
        self.position = 0
        self.positions = len(self.figure)
        self.state = self.figure[self.position]

    def rotate_right(self):
        """ Switch positions from figure positions list """
        # Means only one position no need in switching
        if self.positions == 1:
            return
        elif self.positions > self.position + 1:
            self.position += 1
        else:
            self.position = 0
        self.state = self.figure[self.position]

    def rotate_left(self):
        if self.positions == 1:
            return
        elif self.position == 0:
            self.position = self.positions - 1
        else:
            self.position -= 1
        self.state = self.figure[self.position]

    def __str__(self):
        return '\n'.join(str(line) for line in self.state)
