import pygame
from asteroid import *
from asteroidfield import *
from constants import *
from player import *
from shot import *

def  main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    dt = 0

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for update in updatable:
            update.update(dt)

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game Over!")
                return 
            for shot in shots:
                if shot.is_colliding(asteroid):
                    asteroid.kill()
                    shot.kill()
        
        screen.fill((0,0,0))
        
        for draw in drawable:
            draw.draw(screen)


        pygame.display.flip()
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()