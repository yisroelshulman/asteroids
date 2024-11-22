import pygame
from constants import *
from player import *

def  main():
    print("Starting asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = dt  + (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()