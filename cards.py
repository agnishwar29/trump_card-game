import pygame

class Card:
    """A class to manage the card deck"""
    def __init__(self, ai_game):
        """Initialize the card and set it's position"""
        self.screen = ai_game.screen

        self.screen_rect = ai_game.screen.get_rect()

        #load the card deck image
        self.image1 = pygame.image.load('219525-200.png')
        self.rect1 = self.image1.get_rect()
        self.rect1.midbottom = self.screen_rect.midbottom

        self.image2 = pygame.image.load('219525-200.png')
        self.rect2 = self.image2.get_rect()
        self.rect2.midtop = self.screen_rect.midtop

    def blitme(self):
        self.screen.blit(self.image1, self.rect1)
        self.screen.blit(self.image2, self.rect2)





