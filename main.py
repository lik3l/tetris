import os

import pygame

import modules.constants as c
from modules.game import Game
from modules.board import Board
from modules.helpers import EndGame

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

    myfont = pygame.font.SysFont("monospace", 16)
    end_game = EndGame(myfont, c.WHITE, size, screen, board)
    game = Game(board, pygame, screen, end_game, block_bg, myfont)
    screen.fill(c.GRAY)
    while True:
        game.flow()


if __name__ == '__main__':
    main()
