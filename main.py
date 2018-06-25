from operator import floordiv, sub
import pygame
from pygame.locals import (
    USEREVENT,
)
import sys
import modules.constants as c
from modules.input_handler import input_handler

from modules.board import Board
from modules.helpers import write_end_text

pygame.init()


def main():
    size = c.SCREEN_SIZE
    speed = c.DEFAULT_SPEED
    half = (2, 2)
    black = 0, 0, 0
    white = 255, 255, 255

    board = Board(*size)
    board_rect = pygame.Rect((0, 0, *size))

    screen = pygame.display.set_mode(size)
    board_surf = screen.subsurface(board_rect)

    # events
    MOVEDOWN = USEREVENT+2
    pygame.time.set_timer(MOVEDOWN, speed)

    myfont = pygame.font.SysFont("monospace", 16)

    while True:
        input_handler(pygame, board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOVEDOWN:
                board.move_figure()
        if board.get_game_state():
            screen.fill(black)
            # pygame.draw.rect(screen, white, (0, 0, *board.get_pixel_size()), 1)
            for coords in board.print_board():
                pygame.draw.rect(board_surf, white, coords)
            for coords in board.print_figure():
                pygame.draw.rect(board_surf, white, coords)
            scoretext = myfont.render(board.score.get_score(), 1, white)
            screen.blit(scoretext, (5, 10))
            pygame.display.flip()
        elif board.get_score_state():
            screen.fill(black)

            text_list = list()
            text_list.append(myfont.render("Game over", 1, white))
            text_list.append(myfont.render(board.score.get_score_end(), 1, white))

            write_end_text(screen, text_list, size)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.key == pygame.K_RETURN:
                        board.score.write_top_score()
                        board.end_score_state()
                    else:
                        board.score.update_player_name(str(event.unicode))
        else:
            break


if __name__ == '__main__':
    main()
