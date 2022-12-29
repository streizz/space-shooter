import json


class Stats:
    def __init__(self, curlvl):
        self.score = 0
        self.curlvl = curlvl
        with open('spaceship.json', 'r') as f:
            self.scoreupdate = json.load(f)
            self.high_score = self.scoreupdate[f'currecordlvl{self.curlvl}']

    def update_high_score(self):
        with open('temp.json', 'r') as f:
            temp = json.load(f)
            temp['stats'] = self.score
        if self.score > self.high_score:
            self.scoreupdate[f'currecordlvl{self.curlvl}'] = self.score
            with open('spaceship.json', 'w') as f:
                json.dump(self.scoreupdate, f)
            temp['win'] = 1
        with open('temp.json', 'w') as f:
            json.dump(temp, f)
