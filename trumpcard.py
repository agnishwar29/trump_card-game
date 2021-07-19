import sys
import pygame
from settings import Settings
from cards import Card
from card import SCard
import random

class TrumpCard:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.num_games = 26

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Tram card simulator")
        self.card = Card(self)
        self.single_card = SCard(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.single_card.placed = True
                #elif event.key == pygame.K_SPACE:
                    #self.single_card.new_betting = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.single_card.placed = False






    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self.check_events()
            self.single_card.update()

            self.update_screen()


    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.card.blitme()
        self.single_card.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = TrumpCard()
    ai.run_game()
