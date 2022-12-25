import json


class Stats:
    def __init__(self, curlvl):
        self.score = 0
        self.curlvl = curlvl
        with open('spaceship.json', 'r') as f:
            self.scoreupdate = json.load(f)
            self.high_score = self.scoreupdate[f'currecordlvl{self.curlvl}']

    def update_high_score(self):
        if self.score > self.high_score:
            self.scoreupdate[f'currecordlvl{self.curlvl}'] = self.score
            with open('spaceship.json', 'w') as f:
                json.dump(self.scoreupdate, f)