# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    # main game-loop
    while True:
        screen.fill(colours["b"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
