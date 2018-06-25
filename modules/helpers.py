from json import loads


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
        prev_height = text.get_height()


def get_scores():
    """ Get scores from file """
    with open('scores.json') as f:
        scores = loads(f.read())
    return scores
