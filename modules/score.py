import json
from . import constants as c
from .helpers import get_scores


class Score:
    def __init__(self):
        self.score = 0
        self.top_scores = get_scores()
        self.player_name = ''

    def __str__(self):
        return 'Score: {}'.format(self.score)

    def increase_score(self, count):
        """ Increases score """
        self.score += count ** c.MULTI_LINE_MULTIPLIER * c.LINE_COST

    def get_score(self):
        return 'Your score: {}'.format(self.score)

    def check_score(self):
        return self.score >= self.top_scores[-1]['score']

    def get_score_end(self):
        return 'Your score is: {}'.format(self.score)

    def get_score_list(self):
        """ Returns top scores list """
        return ['{}: {}'.format(x['name'], x['score']) for x in self.top_scores]

    def write_top_score(self):
        """ Write user score to rating """
        self.top_scores.append({'name': self.player_name, 'score': self.score})
        f = open('scores.json', 'w')
        f.write(json.dumps(sorted(self.top_scores, key=lambda x: x['score'], reverse=True)[:10]))
        f.close()

    def update_player_name(self, key):
        if key == 'BACKSPACE':
            self.player_name = self.player_name[:-1]
        else:
            self.player_name += key.upper()

    def get_player_name(self):
        return self.player_name
