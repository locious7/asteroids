import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for update in updatable:
            update.update(dt)

        screen.fill(SCREEN_COLOR) 

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()