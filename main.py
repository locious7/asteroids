import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(SCREEN_COLOR) 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()


if __name__ == "__main__":
    main()