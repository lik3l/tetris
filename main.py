import os

import pygame

import modules.constants as c
from modules.flow_handlers import game_flow_handler, score_flow_handler
from modules.game import Game
from modules.input_handler import end_game_state_handler
from modules.board import Board
from modules.helpers import write_end_text, enter_player_name, draw_rect, get_board_color, EndGame, get_not_scored

pygame.init()
pygame.key.set_repeat(300, 50)  # 300 pause before repeat


def main():
    size = c.SCREEN_SIZE

    board = Board(*size)

    screen = pygame.display.set_mode(size)

    # load bg
    block_bg = pygame.transform.scale(
        pygame.image.load(os.path.join('static', 'block_bg.png')),
        board.get_block_size()
    )

    # TODO: move speed to game

    myfont = pygame.font.SysFont("monospace", 16)
    end_game = EndGame(myfont, c.WHITE, size, screen, board)
    game = Game(board, pygame, screen, end_game)
    game.init_timer()
    screen.fill(c.GRAY)
    while True:
        if game.get_state() == game.GAME_STATE:
            """ Game running state """
            for event in pygame.event.get():
                game_flow_handler(event, pygame, board, game)

            if not game.is_paused():
                game.board_surf.fill(c.BLACK)
                for coords in board.print_board():
                    draw_rect(game.board_surf, get_board_color(board.get_fullness()), coords, block_bg)
                for coords in board.print_figure():
                    draw_rect(game.board_surf, board.figure.get_color(), coords, block_bg)
            else:
                write_end_text(screen, [myfont.render('Paused', 1, c.WHITE)], size)

            scoretext = myfont.render(board.score.get_score(), 1, c.WHITE)
            game.board_surf.blit(scoretext, (5, 10))
            if board.score.get_int_score() >= 100 * game.get_round():
                game.next_round()
            pygame.display.flip()
        elif game.get_state() == game.SCORE_STATE:
            """ Show and input score """
            screen.fill(c.BLACK)

            if not board.score.check_score():
                text = get_not_scored(myfont, board, c.WHITE)
            else:
                text = enter_player_name(myfont, board, c.WHITE)
            write_end_text(screen, text, size)

            for event in pygame.event.get():
                score_flow_handler(event, pygame, board)

            pygame.display.flip()

        elif game.get_state() == game.ENDGAME_STATE:
            screen.fill(c.BLACK)

            end_game.draw()
            for event in pygame.event.get():
                end_game_state_handler(event, pygame, game)
            pygame.display.flip()
        else:
            # TODO: Add watch score screen in menu
            break


if __name__ == '__main__':
    main()
