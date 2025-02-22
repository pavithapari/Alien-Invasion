import pygame
class Settings:
    def __init__(self,):
        pygame.init()
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.screenWidth=(self.screen_width,self.screen_height)
        self.level=1
        self.bg=(230,230,230)
        self.bullet_speed=2
        self.bullet_width=4
        self.bullet_height=17
        self.no_of_bullets=3
        self.alien_speed=0.5
        self.ship_limits=3
        self.score=0
        self.points=50
    def levOne(self):
        self.level=1
        self.bullet_width=5
        self.bullet_speed=2
        self.alien_speed=0.4
        self.ship_limits=3
        self.points=50
        
    def levTwo(self):
        self.level=2
        self.bullet_width=4
        self.bullet_speed=3
        self.alien_speed=0.8
        self.ship_limits=3
        self.points=100
    def levThree(self):
        self.level=3
        self.bullet_width=3
        self.bullet_speed=3
        self.alien_speed=1
        self.ship_limits=3
        self.points=150   
        
