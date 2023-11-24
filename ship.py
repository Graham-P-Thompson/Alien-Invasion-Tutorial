import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    #ai_game is the current instance AlienInvasion class.
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect(rectangle).
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ships horizontal position because
        #pygame rect attributes such as x store only integers, casting is needed.
        self.x = float(self.rect.x)

        #Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ships position based on the movement flags."""
        #Seperate if statements makes it move effective incase both keys
        #are held down at the same time, if it was elif right would have priority
        #Update the ships x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
