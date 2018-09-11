import sys
from modules import constants as c
from modules.input_handler import input_handler, input_up_handler

# Hack, shame on me ;)
k_down_pressed = False


def game_flow_handler(event, pygame, board, game, speed):
    global k_down_pressed
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == c.MOVEDOWN:
        if not board.move_figure():
            pygame.time.set_timer(c.MOVEDOWN, speed)
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            if not game.is_paused():
                pygame.time.set_timer(c.MOVEDOWN, 0)
            else:
                pygame.time.set_timer(c.MOVEDOWN, speed)
            game.pause()
        elif event.key == pygame.K_DOWN:
            if not k_down_pressed:
                pygame.time.set_timer(c.MOVEDOWN, 20)
            k_down_pressed = True
        elif not game.is_paused():
            input_handler(pygame, board)
    if event.type == pygame.KEYUP and not game.is_paused():
        if event.key == pygame.K_DOWN:
            k_down_pressed = False
        input_up_handler(pygame, speed)


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