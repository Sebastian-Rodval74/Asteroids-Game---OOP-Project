import pygame
import traceback
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Constants 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Asteroids Game")
        clock = pygame.time.Clock()
        running = True

        # Sprite groups
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots_group = pygame.sprite.Group()

        # Set containers BEFORE instantiation
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable,)
        Player.containers = (updatable, drawable)
        Shot.containers = (shots_group, updatable, drawable)

        # Create game objects
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        field = AsteroidField()

        # Game loop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            dt = clock.tick(60) / 1000  # Delta time in seconds

            # Update all objects
            updatable.update(dt)
            for asteroid in asteroids:
                if player.collide(asteroid):
                    print("Game over!")
                    running = False
                    break

            for asteroid in asteroids:
                for shot in shots_group:
                    if shot.collide(asteroid):
                        asteroid.kill()
                        shot.kill()
                        break
                
            # Clear the screen
            screen.fill("black")

            # Draw all drawable objects
            for sprite in drawable:
                sprite.draw(screen)

            # Update the display
            pygame.display.flip()

    except Exception as e:
        print(f"Error: {e}")
        print(traceback.format_exc())
        input("Press Enter to exit...")

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()