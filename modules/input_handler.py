from pygame import locals as c


def left(board):
    board.figure_left()


def right(board):
    board.figure_right()


def s_down(board):
    board.speed_down()


def r_right(board):
    board.rotate_right()


def r_left(board):
    board.rotate_left()


pressed_keys_map = {
    c.K_LEFT: {'count': 0, 'action': left, 'wait': True},
    c.K_RIGHT: {'count': 0, 'action': right, 'wait': True},
    c.K_DOWN: {'count': 0, 'action': s_down, 'wait': False},
    c.K_SPACE: {'count': 0, 'action': r_right, 'wait': True},
    c.K_LALT: {'count': 0, 'action': r_left, 'wait': True},
}


def input_handler(pygame, board):
    pressed = pygame.key.get_pressed()
    for k in pressed_keys_map:
        if pressed[k]:
            if not pressed_keys_map[k]['wait'] \
                    or pressed_keys_map[k]['count'] > 1 \
                    or not pressed_keys_map[k]['count']:
                pressed_keys_map[k]['action'](board)
                pygame.display.flip()
            pressed_keys_map[k]['count'] += 1


def input_up_handler(pygame):
    pressed = pygame.key.get_pressed()
    for k in pressed_keys_map:
        if not pressed[k]:
            pressed_keys_map[k]['count'] = 0
