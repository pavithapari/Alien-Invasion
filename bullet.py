from pygame.sprite import Sprite
import pygame
import my_first

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.setting
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)
        self.colour = (255,255,255)

    def update(self):
        # Move the bullet up the screen
        self.y -= self.settings.bullet_speed
        # Update the rectangle's position
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)
        

# Example usage (make sure to replace this with your actual game loop)
# ai_game = ... (Your game instance here)
# bullet = Bullet(ai_game)
# bullet.update()
# bullet.draw_bullet()
