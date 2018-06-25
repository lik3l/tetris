import pygame
from pygame.locals import (
    USEREVENT,
)
import sys
import modules.constants as c
from modules.input_handler import input_handler

from modules.board import Board
from modules.helpers import write_end_text, enter_player_name

pygame.init()
pygame.key.set_repeat(500, 50)


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
        if board.get_game_state():
            input_handler(pygame, board)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == MOVEDOWN:
                    board.move_figure()

            screen.fill(black)
            for coords in board.print_board():
                pygame.draw.rect(board_surf, white, coords)
            for coords in board.print_figure():
                pygame.draw.rect(board_surf, white, coords)
            scoretext = myfont.render(board.score.get_score(), 1, white)
            screen.blit(scoretext, (5, 10))
            pygame.display.flip()
        elif board.get_score_state():
            screen.fill(black)

            text = enter_player_name(myfont, board, white)
            write_end_text(screen, text, size)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.key == pygame.K_RETURN:
                        board.score.write_top_score()
                        board.end_score_state()
                    else:
                        key = str(event.unicode) if not event.key == pygame.K_BACKSPACE else 'BACKSPACE'
                        board.score.update_player_name(key)

            pygame.display.flip()
        else:
            break


if __name__ == '__main__':
    main()
