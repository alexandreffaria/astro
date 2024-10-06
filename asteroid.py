from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random


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
        rotatePlus = self.velocity.rotate(angle)
        rotateMinus = self.velocity.rotate(-angle)

        newRadius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, newRadius)
        a1.velocity = rotatePlus  * 1.2
        a2 = Asteroid(self.position.x, self.position.y, newRadius)
        a2.velocity = rotateMinus * 1.2 
