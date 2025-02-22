import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.setting=ai_game.setting
        self.img=pygame.image.load("D:/myProjects/alienInvasion/assests/new_alien_1-removebg-preview.png")
        self.image=pygame.transform.scale(self.img,(75,75))
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update_alien(self):
        self.y+= self.setting.alien_speed
        self.rect.y=self.y


