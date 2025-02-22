import pygame
import random
import sys

import pygame.image
from settings import Settings
from ship import Ship 
from bullet import Bullet
import sys
from reset import GameStatics 
from time import sleep
from alien import Alien
from button import Button
from scoreBoard import Scoreboard
import time
pygame.mixer.init()
from backgroundscreen import Bg

class AlienInvasion:
    def __init__(self,settings):
        pygame.init()
        self.setting = settings
        self.bg=Bg()
        print(self.setting.alien_speed)  
        self.screen = pygame.display.set_mode(self.setting.screenWidth,)
        self.screen_rext=self.screen.get_rect()
        print(self.setting.screenWidth)
        self.ship_left=self.setting.ship_limits
        self.game_active=True
        self.score=self.setting.score
        self.bullet=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self.alien=Alien(self)
        self._fleet_()
        self.clock = pygame.time.Clock()
        self.ship=Ship(self)
        self.right=False
        self.re=GameStatics(self)
        self.sb=Scoreboard(self)
        pygame.mixer.music.load("D:/myProjects/alienInvasion/assests/game-music-loop-7-145285.mp3")
        self.bullet_sound=pygame.mixer.Sound("D:/myProjects/alienInvasion/assests/retro-laser-1-236669.mp3")
        self.game_over=pygame.mixer.Sound("D:/myProjects/alienInvasion/assests/083822_8-bit-quotgame-overquot-82872.mp3")
        self.collision_sound=pygame.mixer.Sound("D:/myProjects/alienInvasion/assests/thud-291047.mp3")
        pygame.mixer.music.play(-1)
        self.game_start=pygame.mixer.Sound("D:/myProjects/alienInvasion/assests/game-start-6104.mp3")
        self.hit_sound=pygame.mixer.Sound("D:/myProjects/alienInvasion/assests/error-4-199275.mp3")
        self.high_sound=pygame.mixer.Sound("D:/myProjects/alienInvasion/assests/magical-twinkle-242245.mp3")
        pygame.display.set_caption("ALIEN INVASION GAME")
        self.font=pygame.font.SysFont("Ariel",48,bold=True)
        self.new_high_score=False
        self.rungame()
     
        
        
        

    def rungame(self):
        while True:
            self._check_events()


            if self.game_active:
                 self.bg.update()
                 self.ship.update()
                 self.bullet.update()
                 for alien in self.aliens.sprites():
                     alien.update_alien()
                 for i in self.bullet.copy() :
                     if i.rect.bottom<=0:
                         self.bullet.remove(i)
            if self.game_active==False:
                 pygame.quit
                 break

            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        self.ship.right=True
                    if event.key==pygame.K_LEFT:
                         self.ship.left=True
                    if event.key==pygame.K_UP:
                         self.ship.up=True
                    if event.key==pygame.K_DOWN:
                         self.ship.down=True
                    if event.key==pygame.K_SPACE:
                         self._runGame_()
                         self.bullet_sound.play()
                    if event.key==pygame.K_p:
                         self.game_active=True
                         pygame.mouse.set_visible(False)
                    if event.key==pygame.K_q:
                         sys.exit()
                    if event.key==pygame.K_RETURN:
                         self.main=True
                elif event.type==pygame.KEYUP:
                     if event.key==pygame.K_RIGHT:
                          self.ship.right=False
                     if event.key==pygame.K_LEFT:
                          self.ship.left=False
                     if event.key==pygame.K_UP:
                         self.ship.up=False
                     if event.key==pygame.K_DOWN:
                         self.ship.down=False

                
                    
    def _runGame_(self):
          new_bullets=Bullet(self)
          self.bullet.add(new_bullets) 

    def _update_screen(self):
            self.bg.update()
            self.bg.draw()
            self.aliens.draw(self.screen)
            self.draw_lives()

            self.ship.blitme()
            self.aliens.draw(self.screen)
            for bullet in self.bullet.sprites():
                 bullet.draw_bullet()
            collisions=pygame.sprite.groupcollide(self.bullet,self.aliens,True,True)
            if pygame.sprite.spritecollideany(self.ship,self.aliens):
                 self._ship_hit_()
                 pygame.display.flip()
            if collisions:
                 self.collision_sound.play()
                 self.re.score +=self.setting.points*len(collisions)
                 if self.re.high_score<self.re.score:
                      self.re.high_score=self.re.score
                      self.sb.prep_high_score()
                      self.re.save_high_score()
                      if not hasattr(self, "new_high_score") or not self.new_high_score:
                         self.new_high_score = True 
                         high_score_msg = self.font.render("You reached a high score!", True, ((255, 0, 255)))
                         msg_rect = high_score_msg.get_rect()              
                         msg_rect.center = self.screen.get_rect().center
                         self.high_sound.play()
                         self.screen.blit(high_score_msg,msg_rect)
                         pygame.display.flip()
                         pygame.time.delay(2000)  
          
                 self.sb.prep()
           

            
            if not self.aliens:
                 self._fleet_()
            self.alien_bottom()
              
            self.sb.show_score()
               

            
               
            pygame.display.flip()
     
    def alien_bottom(self):
         for alien in self.aliens.sprites():
              if alien.rect.bottom > self.setting.screenWidth[1]:
                   self._ship_hit_()
              
    def _ship_hit_(self):
          if self.ship_left > 1:
               self.hit_sound.play()
               self.overlay = pygame.Surface(self.setting.screenWidth, pygame.SRCALPHA)
               self.overlay.fill((0, 0, 0, random.randint(250, 255)))  # Last value is the alpha (transparency)

    # Draw the object on the overlay
               pygame.draw.rect(self.overlay, (255, 255, 255, random.randint(254, 255)),self.screen_rext)

    # Blit the overlay onto the screen
               self.screen.blit(self.overlay, (0, 0))
               
               
               self.ship_left-=1
               self.aliens.empty()
               self.bullet.empty()
               self.ship.center()
               self._fleet_()
               sleep(0.3)
               self.play=True
          else:
               self.game_active=False
               self.re.save_high_score()
               pygame.mouse.set_visible(True)
               if self.play:
                    self.game_over.play()
                    self.play=False
               
               
            
           
    def _fleet_(self):
         #the alien loop for gird view
         alien=Alien(self)
         alien_width,alien_height=alien.rect.size
         current_x=alien_width*3
         current_y=0
         while current_y < self.setting.screenWidth[1]-7*alien_height:
              while current_x < self.setting.screenWidth[0]-(3*alien_width):
                   new_alien=Alien(self)
                   new_alien.x=current_x
                   new_alien.y=current_y
                   new_alien.rect.x=current_x
                   new_alien.rect.y=current_y
                   self.aliens.add(new_alien)
                   current_x=current_x+(2*alien_width)
              current_y=current_y+(alien_height*1.5)
              current_x = alien_width*3  # Reset to the starting x position for the new row
    def draw_lives(self):
         self.image=pygame.image.load("D:/myProjects/alienInvasion/assests/WhatsApp_Image_2025-02-06_at_3.30.10_PM-removebg-preview.bmp")
         self.image=pygame.transform.scale(self.image,(60,48))
         for i in range(self.ship_left):
              self.screen.blit(self.image,(0+i*60,90))




