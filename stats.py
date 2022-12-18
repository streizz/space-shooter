class Stats:
    def __init__(self):
        self.score = 0
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore.txt', 'w') as f:
                f.write(str(self.high_score))