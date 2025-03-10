#!/usr/bin/env python3
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        return

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        return

    def update(self, dt):
        self.position += self.velocity * dt
