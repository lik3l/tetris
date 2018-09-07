from json import loads

from pygame import Color, Surface, SRCALPHA, transform, draw, BLEND_RGBA_MAX, BLEND_RGBA_MIN
from pygame.rect import Rect

from modules import constants as c


def write_end_text(screen, text_list, size):
    """
    Writes text to a center of the screen
    size: tuple, screen size
    screen: screen object,
    text_list: list of text surfaces
    """
    prev_height = 0
    text_height = sum([x.get_height() for x in text_list])
    for text in text_list:
        screen.blit(
            text,
            (
                size[0] // 2 - text.get_width() // 2,
                size[1] // 2 - text_height // 2 + prev_height
            )
        )
        prev_height += text.get_height()


def get_scores():
    """ Get scores from file """
    with open('scores.json') as f:
        scores = loads(f.read())
    return scores


def update_timer(speed, pygame, g_round):
    new_speed = int(speed * .9)
    pygame.time.set_timer(c.MOVEDOWN, new_speed)
    return new_speed, g_round + 1


def get_board_color(fullness):
    if fullness > .75:
        return c.RED
    elif fullness > .5:
        return c.YELLOW
    elif fullness > .25:
        return c.YGREEN
    else:
        return c.GREEN


def enter_player_name(myfont, board, color):
    """ Username entering """
    text_list = list()
    text_list.append(myfont.render("Game over", 1, color))
    text_list.append(myfont.render(" ", 1, color))
    text_list.append(myfont.render("Top Scores", 1, color))
    for score in board.score.get_score_list():
        text_list.append(myfont.render(score, 1, color))
    text_list.append(myfont.render(" ", 1, color))
    text_list.append(myfont.render(board.score.get_score_end(), 1, color))
    text_list.append(myfont.render("Enter your name", 1, color))
    text_list.append(myfont.render(board.score.get_player_name(), 1, color))

    return text_list


def draw_rect(surface, color, rect, radius=0.3):
    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect = Rect(rect)
    color = Color(*color)
    alpha = color.a
    color.a = 0
    pos = rect.topleft
    rect.topleft = 0, 0
    rectangle = Surface(rect.size, SRCALPHA)

    circle = Surface([min(rect.size) * 3] * 2, SRCALPHA)
    draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
    circle = transform.smoothscale(circle, [int(min(rect.size) * radius)] * 2)

    radius = rectangle.blit(circle, (0, 0))
    radius.bottomright = rect.bottomright
    rectangle.blit(circle, radius)
    radius.topright = rect.topright
    rectangle.blit(circle, radius)
    radius.bottomleft = rect.bottomleft
    rectangle.blit(circle, radius)

    rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
    rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))

    rectangle.fill(color, special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255, 255, 255, alpha), special_flags=BLEND_RGBA_MIN)

    return surface.blit(rectangle, pos)
