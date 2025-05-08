import pygame  
from constants import PLAYER_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.rotation_speed = 0.5  # degrees per second

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
