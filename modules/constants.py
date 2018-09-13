from pygame.locals import USEREVENT

Z = 0
S = 1
O = 2
L = 3
J = 4
I = 5
W = 6

FIGURE_TYPES = [Z, S, O, L, J, I, W]

MOVEDOWN = USEREVENT + 2
MOVELEFT = USEREVENT + 3
MOVERIGHT = USEREVENT + 4
ROTATERIGHT = USEREVENT + 5
ROTATELEFT = USEREVENT + 6
# do not modify order
EVENTS = [MOVELEFT, MOVERIGHT, MOVEDOWN, ROTATERIGHT, ROTATELEFT]
DEFAULT_EVENT_TIMER = 200
FAST_EVENT_TIMER = 20

# Colors
BLACK = [0, 0, 0]
GRAY = [20, 20, 20]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [55, 185, 40]
YGREEN = [157, 187, 37]
YELLOW = [222, 177, 48]

LEFT = 0
RIGHT = 1
DOWN = 2
R_RIGHT = 3
R_LEFT = 4
MOVE_ACTIONS = [LEFT, RIGHT, DOWN, R_RIGHT, R_LEFT]

DEFAULT_SPEED = 1000

COLORS = (
    (255, 255, 255),
    (50, 255, 255),
    (255, 50, 255),
    (255, 255, 50),
    (50, 50, 255),
    (255, 50, 50),
    (50, 255, 50),
)

LINE_COST = 10
MULTI_LINE_MULTIPLIER = 2

# Default width board size in blocks
# For now field is 1:2 ratio, later calculations expect that
DEFAULT_WIDTH = 9
DEFAULT_HEIGHT = DEFAULT_WIDTH * 2

SCREEN_SIZE = (640, 480)

FIGURE_FORMS = {
    W: (
        (
            (0, 1, 0, 0),
            (0, 1, 1, 0),
            (0, 1, 0, 0),
            (0, 0, 0, 0),
        ),
        (
            (0, 0, 0, 0),
            (1, 1, 1, 0),
            (0, 1, 0, 0),
            (0, 0, 0, 0),
        ),
        (
            (0, 1, 0, 0),
            (1, 1, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 0, 0),
        ),
        (
            (0, 1, 0, 0),
            (1, 1, 1, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
        ),
    ),
    L: (
        (
            (0, 1, 0, 0),
            (0, 1, 0, 0),
            (0, 1, 1, 0),
            (0, 0, 0, 0),
        ),
        (
            (0, 0, 0, 0),
            (0, 1, 1, 1),
            (0, 1, 0, 0),
            (0, 0, 0, 0),
        ),
        (
            (0, 0, 0, 0),
            (0, 1, 1, 0),
            (0, 0, 1, 0),
            (0, 0, 1, 0),
        ),
        (
            (0, 0, 0, 0),
            (0, 0, 1, 0),
            (1, 1, 1, 0),
            (0, 0, 0, 0),
        ),
    ),
    Z: (
        (
            (0, 0, 0, 0),
            (0, 1, 1, 0),
            (0, 0, 1, 1),
            (0, 0, 0, 0),
        ),
        (
            (0, 0, 0, 0),
            (0, 0, 1, 0),
            (0, 1, 1, 0),
            (0, 1, 0, 0),
        ),
    ),
    S: (
        (
            (0, 0, 0, 0),
            (0, 1, 1, 0),
            (1, 1, 0, 0),
            (0, 0, 0, 0),
        ),
        (
            (0, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 1, 1, 0),
            (0, 0, 1, 0),
        ),
    ),
    J: (
        (
            (0, 0, 1, 0),
            (0, 0, 1, 0),
            (0, 1, 1, 0),
            (0, 0, 0, 0),
        ),
        (
            (0, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 1, 1, 1),
            (0, 0, 0, 0),
        ),
        (
            (0, 0, 0, 0),
            (0, 1, 1, 0),
            (0, 1, 0, 0),
            (0, 1, 0, 0),
        ),
        (
            (0, 0, 0, 0),
            (1, 1, 1, 0),
            (0, 0, 1, 0),
            (0, 0, 0, 0),
        ),
    ),
    O: (
        (
            (0, 0, 0, 0),
            (0, 1, 1, 0),
            (0, 1, 1, 0),
            (0, 0, 0, 0),
        ),
    ),
    I: (
        (
            (0, 0, 1, 0),
            (0, 0, 1, 0),
            (0, 0, 1, 0),
            (0, 0, 1, 0),
        ),
        (
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (1, 1, 1, 1),
            (0, 0, 0, 0),
        ),
    )
}
