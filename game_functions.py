import sys
import pygame

def check_events(space_ship):
    # Listen for keyboard and mouse envents
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #When Pygame detects KEYDOWN event I check if right key is pressed. If so increse position for 1 pixel
        #KEYDOWN == when key is pressed down, KEYUP == when key is released

        #IF right key is pressed ship is moving right
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                space_ship.moving_right = True

        #IF the right key is released ship has stopped moving right
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                space_ship.moving_right = False


def update_screen(ai_settings, screen, ship):

    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()


    # Make the most recently drawn screen visible
    pygame.display.flip()