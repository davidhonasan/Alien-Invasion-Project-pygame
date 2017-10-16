import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    # Make a ship
    ship = Ship(settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    pygame.display.set_caption("Alien Invader Game")

    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(settings, screen, ship, bullets)

run_game()