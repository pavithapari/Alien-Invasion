import json
class GameStatics:
    def __init__(self,ai_game):
        self.score=ai_game.score
        self.high_score=self.load_high_score()
        self.is_high=False
        
    def save_high_score(self):
        self.is_high=True
        with open('high_score.json', 'w') as f:
            json.dump(self.high_score, f)

    def load_high_score(self):
        try:
            with open('high_score.json') as f:
                return json.load(f)
        except FileNotFoundError:
            return 0    
    def reset(self):
        self.score=0
    