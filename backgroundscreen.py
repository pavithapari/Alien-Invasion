import pygame
import sys
class Bg:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        print(self.screen_height,self.screen_width)

        self.screen=pygame.display.set_mode((self.screen_width,self.screen_height))
        self.image1=pygame.image.load("D:/myProjects/alienInvasion/assests/sample webpage.bmp")
        self.image=pygame.transform.scale(self.image1,(self.screen_width,self.screen_height))

        self.bg_1=0
        self.bg_2=-self.screen_height
        self.clock=pygame.time.Clock()

        """ while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()"""
    def update(self):
        self.bg_1+=0.9
        self.bg_2+=0.9
        if self.bg_1>=self.screen_height:
             self.bg_1=-self.screen_height
        if self.bg_2>=self.screen_height:
             self.bg_2=-self.screen_height
    def draw(self):
        self.screen.blit(self.image,(0,self.bg_1))
        self.screen.blit(self.image,(0,self.bg_2))
        
            
