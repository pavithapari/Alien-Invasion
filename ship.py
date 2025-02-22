import pygame
from pygame import event
class Ship:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.image=pygame.image.load("D:/myProjects/alienInvasion/assests/WhatsApp_Image_2025-02-06_at_3.30.10_PM-removebg-preview.bmp")
        self.rect=pygame.Rect(0,0,125,125)
        self.loaded=pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        print(self.rect)
        self.rect.midbottom=self.screen_rect.midbottom
        self.right=False
        self.left=False
        self.up=False
        self.down=False
    def update(self):
        if self.right and self.rect.right < self.screen_rect.right:
            self.rect.x+=5
        if self.left and self.rect.left > self.screen_rect.left:
            self.rect.x-=5
        if self.down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y+=2.5
        if self.up and self.rect.top > self.screen_rect.top:
            self.rect.y-=2.5
    def center(self):
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.loaded,self.rect)
