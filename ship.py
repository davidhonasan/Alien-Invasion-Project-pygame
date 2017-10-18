import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, settings, screen):
        # Initialize the ship and set its starting position.
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the ship image
        self.image = pygame.image.load("images/ship.bmp")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        # Update rect object from self.center.
        self.rect.centerx = self.center

    # This function is used to draw ship
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # The blit function is used to draw the image on the screen

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx