import pygame  
import random
from constants import PLAYER_RADIUS, ASTEROID_MIN_RADIUS
from circleshape import CircleShape



class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.rotation_speed = 0.5  # degrees per second

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            
        )
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split (self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        new_velocity1 *= 1.2
        new_velocity2 *= 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1
        asteroid2.velocity = new_velocity2

        for group in self.groups():
            group.add(asteroid1)
            group.add(asteroid2)    


 # Add to the same group as the original asteroid

    


