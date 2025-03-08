#!/usr/bin/env python3
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        return

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        return

    def update(self, dt):
        self.position += self.velocity * dt
