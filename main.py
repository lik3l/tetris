import pygame
from pygame.locals import (
    USEREVENT,
)
import sys
import modules.constants as c
from modules.input_handler import input_handler

from modules.board import Board

pygame.init()


def main():
    size = c.SCREEN_SIZE
    # speed = [1, 1]
    black = 0, 0, 0
    white = 255, 255, 255

    board = Board(*size)
    board_rect = pygame.Rect((0, 0, *size))

    screen = pygame.display.set_mode(size)
    board_surf = screen.subsurface(board_rect)

    # events
    MOVEDOWN = USEREVENT+2
    pygame.time.set_timer(MOVEDOWN, 1000)

    while True:
        input_handler(pygame, board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOVEDOWN:
                board.move_figure()

        screen.fill(black)
        # pygame.draw.rect(screen, white, (0, 0, *board.get_pixel_size()), 1)
        for coords in board.print_board():
            pygame.draw.rect(board_surf, white, coords)
        for coords in board.print_figure():
            pygame.draw.rect(board_surf, white, coords)
        pygame.display.flip()


if __name__ == '__main__':
    main()
