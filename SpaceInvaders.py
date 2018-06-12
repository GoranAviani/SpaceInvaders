import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    #Initialize pygame, settings and screen
    pygame.init()
    ai_settings = Settings()


    #Create a display window called "screen" , on which all of the games graphical elements will be drawn.
    #screen = pygame.display.set_mode((1200, 800))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Space invaders by Goran Aviani")

    #make a ship
    ship = Ship(screen)


    #Start the main loop of the game
    while True:

        #Listen for keyboard and mouse envents
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #Make the most recently drawn screen visible
        pygame.display.flip()





if __name__ == "__main__":
    run_game()