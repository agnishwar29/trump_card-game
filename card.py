import pygame
import random
from settings import Settings

player_power = random.randint(100,1000)
bot_power = random.randint(100,1000)
str_power = str(player_power)
str_bot_power = str(bot_power)



class SCard:
    """A class to manage the card"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.player_points = 0

        # load the card deck image
        self.image = pygame.image.load('trumpcard[green].jpg')  #player's card
        self.image1 = pygame.image.load('trumpcard[red].jpg')   #bot's card
        self.rect = self.image.get_rect()
        self.rect1 = self.image1.get_rect()


        self.rect.midbottom = self.screen_rect.midbottom   #player's card position
        self.rect1.midtop = self.screen_rect.midtop   #bot's card position

        self.pos = (300,300)
        self.pos1 = (800,300)
        self.player_text_pos = (342,350)
        self.bot_text_pos = (845, 350)
        self.text_pos = (565,350)


        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.placed = False
        self.new_betting = False

        self.font = pygame.font.Font('freesansbold.ttf', 20)

        self.player_text = self.font.render(str_power, True, 'black')
        self.rect2 = self.player_text.get_rect()
        self.bot_text = self.font.render(str_bot_power, True, 'black')
        self.rect3 = self.bot_text.get_rect()

    def betting(self):
        if int(player_power) > int(bot_power):
            self.text = self.font.render('You won', True, 'black')
            self.rect4 = self.text.get_rect()
        elif int(player_power) < int(bot_power):
            self.text = self.font.render('Bot won', True, 'black')
            self.rect4 = self.text.get_rect()



    def update(self,):
        if self.placed :
            self.rect = self.pos
            self.rect1 = self.pos1
            self.rect2 = self.player_text_pos
            self.rect3 = self.bot_text_pos
            self.rect4 = self.text_pos



    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image1, self.rect1)
        self.screen.blit(self.player_text,self.rect2)
        self.screen.blit(self.bot_text, self.rect3)
        self.update()
        self.betting()
        self.screen.blit(self.text, self.rect4)

