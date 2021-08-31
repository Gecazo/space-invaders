import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.space_ship = pygame.image.load('/Users/gecazo/Documents/GitHub/space-invaders/images/ship.bmp')
        self.rect = self.space_ship.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.space_ship, self.rect)