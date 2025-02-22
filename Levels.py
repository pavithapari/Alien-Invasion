
class Level:
    def __init__(self,settings):
        self.settings=settings
    def levOne(self):
        self.settings.score*=1
        self.settings.alien_speed*=1
        self.settings.bullet_width*=1
    def levTwo(self):
        print("calling")
        self.settings.score*=2
        self.settings.alien_speed*=2
    def levThree(self):
        self.settings.score*=3
        self.settings.alien_speed*=3
        
        
        