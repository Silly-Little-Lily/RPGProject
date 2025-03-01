import pygame
import sys

## Start Module: Pretty screen ##

def run_start_menu(screen):

    pygame.display.set_caption("RPG Game")
    
    # Set up looping sound

    running = True
    while running:
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Add quit handling
    pygame.quit()
    sys.exit()