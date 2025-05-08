import pygame
import traceback
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

updatable = pygame.sprite.Group()
drawable= pygame.sprite.Group()
Player.containers = (updatable, drawable)
updatable.update()
for d in drawable:
    d.draw()
asteroids = pygame.sprite.Group()
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)



def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        running = True

        # Instantiate the Player object
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        asteroif_field = AsteroidField()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the screen
            screen.fill("black")
            
            # Re-render the player
            player.draw(screen)
            
            # Update the display
            pygame.display.flip()
            dt = clock.tick(60 / 1000)
            player.update(dt)

    except Exception as e:
        print(f"Error: {e}")
        print(traceback.format_exc())
        input("Press Enter to exit...")  # This will keep the console open

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()