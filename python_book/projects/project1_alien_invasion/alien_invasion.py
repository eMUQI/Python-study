import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
from game_stats import GameStats
import game_functions as gf


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create a statistics
    stats = GameStats(ai_settings)

    # make a button
    play_button = Button(ai_settings, screen, "Play")

    # Make a ship, a group of bullets, a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # create a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats,
                        play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,  screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, stats, screen, ship,
                         aliens, bullets, play_button)


run_game()
