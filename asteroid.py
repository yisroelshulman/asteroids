import pygame
import random
from circleshape import CircleShape
from constants import *


def spawn( radius, position, velocity):
    asteroid = Asteroid(position.x, position.y, radius)
    asteroid.velocity = velocity

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 

        angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS

        spawn(radius, self.position, velocity1)
        spawn(radius, self.position, velocity2)

        