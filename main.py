import pygame
from constants import *

def main():
    pygame.init()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    running = True  # Add a control variable
    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # This will exit the loop cleanly
                    
            screen.fill((0, 0, 0))
            pygame.display.flip()
            
        except KeyboardInterrupt:
            running = False  # This will catch Ctrl+C
            
    pygame.quit()  # Cleanup pygame before exiting

if __name__ == "__main__":
    main()