import sys
from modules import constants as c
from modules.input_handler import input_handler, input_up_handler


def game_flow_handler(event, pygame, board, game):
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == c.MOVEDOWN:
        if not board.move_figure():
            pygame.time.set_timer(c.MOVEDOWN, game.speed)
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            if not game.is_paused():
                pygame.time.set_timer(c.MOVEDOWN, 0)
            else:
                pygame.time.set_timer(c.MOVEDOWN, game.speed)
            game.pause()
        elif event.key == pygame.K_DOWN:
            if not game.pressed_down():
                pygame.time.set_timer(c.MOVEDOWN, 20)
            game.press_down()
        elif not game.is_paused():
            input_handler(pygame, board)
    if event.type == pygame.KEYUP and not game.is_paused():
        if event.key == pygame.K_DOWN:
            game.up_down()
        input_up_handler(pygame, game.speed)


def score_flow_handler(event, pygame, board):
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            board.score.write_top_score()
            board.end_score_state()
            board.set_end_game()
        elif board.score.check_score():
            key = str(event.unicode) if not event.key == pygame.K_BACKSPACE else 'BACKSPACE'
            board.score.update_player_name(key)
