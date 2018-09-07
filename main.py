import sys

import pygame
from pygame.locals import USEREVENT

import modules.constants as c
from modules.input_handler import input_handler, input_up_handler
from modules.board import Board
from modules.helpers import write_end_text, enter_player_name, draw_rect, get_board_color

pygame.init()
pygame.key.set_repeat(400, 50)


def main():
    size = c.SCREEN_SIZE
    speed = c.DEFAULT_SPEED

    board = Board(*size)
    board_rect = pygame.Rect((size[0]//2 - board.get_pixel_size()[0]//2,
                              0, *board.get_pixel_size()))

    screen = pygame.display.set_mode(size)
    board_surf = screen.subsurface(board_rect)

    # events
    MOVEDOWN = USEREVENT+2
    pygame.time.set_timer(MOVEDOWN, speed)

    myfont = pygame.font.SysFont("monospace", 16)

    while True:
        if board.get_game_state():

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == MOVEDOWN:
                    board.move_figure()
                if event.type == pygame.KEYDOWN:
                    input_handler(pygame, board)
                if event.type == pygame.KEYUP:
                    input_up_handler(pygame)

            screen.fill(c.GRAY)
            board_surf.fill(c.BLACK)
            for coords in board.print_board():
                draw_rect(board_surf, get_board_color(board.get_fullness()), coords)
            for coords in board.print_figure():
                draw_rect(board_surf, board.figure.get_color(), coords)
            scoretext = myfont.render(board.score.get_score(), 1, c.WHITE)
            screen.blit(scoretext, (5, 10))
            pygame.display.flip()
        elif board.get_score_state():
            screen.fill(c.BLACK)

            if not board.score.check_score():
                text = list()
                text.append(myfont.render('Game over'))
                text.append(myfont.render('U R LOOSER!!!'))
            else:
                text = enter_player_name(myfont, board, c.WHITE)
            write_end_text(screen, text, size)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        board.score.write_top_score()
                        board.end_score_state()
                    elif board.score.check_score():
                        key = str(event.unicode) if not event.key == pygame.K_BACKSPACE else 'BACKSPACE'
                        board.score.update_player_name(key)

            pygame.display.flip()
        else:
            break


if __name__ == '__main__':
    main()
