import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(settings, screen, ship, aliens)

    pygame.display.set_caption("Alien Invader Game")

    # Make the Play button.
    play_button = Button(settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)

    while True:
        gf.check_events(settings, screen, stats, sb, play_button, ship,
            aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens,
                bullets)
            gf.update_aliens(settings, screen, stats, sb, ship, aliens,
                bullets)
        gf.update_screen(settings, screen, stats, sb, ship, aliens,
            bullets, play_button)


run_game()
