from .constants import FIGURE_FORMS, FIGURE_TYPES, COLORS
from random import choice


class Figure:
    """
    Base figure model used to describe figure and it's moves
    """

    def __init__(self, figure):
        self.figure = FIGURE_FORMS[figure]
        self.position = 0
        self.positions = len(self.figure)
        self.state = self.figure[self.position]
        self.color = choice(COLORS)

    def get_sprite_size(self):
        """ Returns sprite size, assuming sprite is square """
        return len(self.state)

    def next_right(self):
        """ Returns next right position """
        if self.positions > self.position + 1:
            return self.position + 1
        else:
            return 0

    def get_next_left(self):
        return self.figure[self.next_left()]

    def get_next_right(self):
        return self.figure[self.next_right()]

    def next_left(self):
        """ Returns next left position """
        if self.positions == 1:
            return 0
        elif self.position == 0:
            return self.positions - 1
        else:
            return self.position - 1

    def rotate_right(self):
        """ Switch positions from figure positions list """
        # Means only one position no need in switching
        self.position = self.next_right()
        self.state = self.figure[self.position]

    def rotate_left(self):
        self.position = self.next_left()
        self.state = self.figure[self.position]

    def get_state(self):
        """ Returns figure current state """
        return self.state

    def get_color(self):
        return self.color

    @staticmethod
    def get_random():
        return choice(FIGURE_TYPES)

    def __str__(self):
        return '\n'.join(str(line) for line in self.state)
