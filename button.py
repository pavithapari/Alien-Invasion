import pygame
class Button:
    def __init__(self,ai_game,msg):
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.width,self.height=200,50
        self.button_col=(0,255,0)
        self.text_col=(255,255,255)
        self.font=pygame.font.Font("C:/Users/pavit/myProjects/alienInvasion/BubbleBobble-rg3rx.ttf",48)
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        self.prep(msg)
    def prep(self,msg):
        self.msg_image=self.font.render(msg,False,self.text_col,self.button_col)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    def draw(self):
        self.screen.fill(self.button_col,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)



