import pygame
from reset import GameStatics
class Scoreboard:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.re=ai_game.re
        self.settings=ai_game.setting
        self.screen_rect=self.screen.get_rect()
        self.text_colour=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        self.prep()
        self.lev()
        self.prep_high_score()
    def prep(self):
        self.round=round(int(self.re.score),-1)
        self.score=f"YOUR SCORE: {self.round:,}"
        self.score_image=self.font.render(self.score,True,self.text_colour,self.settings.bg)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20
    
    def lev(self):
        self.level=self.settings.level
        self.level=f"LEVEL :{self.level}"
        self.level_image=self.font.render(self.level,True,self.text_colour,self.settings.bg)
        self.level_rect=self.score_image.get_rect()
        self.level_rect.topleft=(0,20)
        

    def prep_high_score(self):
        high_score_str = f"HIGH SCORE:{self.re.high_score}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_colour, self.settings.bg)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20
        
                      
        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect) 
        
        
        