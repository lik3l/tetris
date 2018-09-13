import sys
from modules import constants as c
from modules.input_handler import input_handler, input_up_handler


def game_flow_handler(event, game):
    if event.type == game.pygame.QUIT:
        sys.exit()
    if event.type == c.MOVEDOWN:
        if not game.board.move_figure():
            game.pygame.time.set_timer(c.MOVEDOWN, game.speed)
    elif event.type == game.pygame.KEYDOWN:
        if event.key == game.pygame.K_ESCAPE:
            if not game.is_paused():
                game.pygame.time.set_timer(c.MOVEDOWN, 0)
            else:
                game.pygame.time.set_timer(c.MOVEDOWN, game.speed)
            game.pause()
        elif event.key in game.keymap.get_keys():
            game.key_down(event.key)
        elif not game.is_paused():
            input_handler(game.pygame, game.board)
    if event.type == game.pygame.KEYUP and not game.is_paused():
        if event.key == game.pygame.K_DOWN:
            game.up_down()
        input_up_handler(game.pygame, game.speed)


def score_flow_handler(event, game):
    if event.type == game.pygame.QUIT:
        sys.exit()
    elif event.type == game.pygame.KEYDOWN:
        if event.key == game.pygame.K_RETURN:
            game.board.score.write_top_score()
            game.board.end_score_state()
            game.board.set_end_game()
        elif game.board.score.check_score():
            key = str(event.unicode) if not event.key == game.pygame.K_BACKSPACE else 'BACKSPACE'
            game.board.score.update_player_name(key)
