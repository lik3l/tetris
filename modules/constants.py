Z = 0
S = 1
O = 2
L = 3
J = 4
I = 5

FIGURE_TYPES = [Z, S, O, L, J, I]

# Default width board size in blocks
# For now field is 1:2 ratio, later calculations expect that
DEFAULT_WIDTH = 8
DEFAULT_HEIGHT = DEFAULT_WIDTH * 2

SCREEN_SIZE = (640, 480)

FIGURE_FORMS = {
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
