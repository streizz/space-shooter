import json


class Stats:
    def __init__(self, curlvl):
        self.score = 0
        self.curlvl = curlvl
        self.bg = 'media/lvl' + str(curlvl) + 'bg.png'
        with open('spaceship.json', 'r') as f:
            self.scoreupdate = json.load(f)
            self.high_score = self.scoreupdate[f'currecordlvl{self.curlvl}']
        with open('temp.json', 'r') as j:
            self.temp = json.load(j)
            self.temp['win'] = 0
            self.temp['stats'] = 0
            self.temp['curbg'] = self.bg
    
    def update_high_score(self):
        self.temp['stats'] = self.score
        if self.score > self.high_score:
            self.scoreupdate[f'currecordlvl{self.curlvl}'] = self.score
            self.high_score = self.score
            with open('spaceship.json', 'w') as z:
                json.dump(self.scoreupdate, z)
            self.temp['win'] = 1
        with open('temp.json', 'w') as p:
            self.temp['curbg'] = self.bg
            self.temp['highscore'] = self.high_score
            json.dump(self.temp, p)