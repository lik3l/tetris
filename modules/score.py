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

    def get_score_end(self):
        return 'Your score is: {}'.format(self.score)

    def get_score_list(self):
        """ Returns top scores list """
        return ['{}: {}'.format(x['name'], x['score']) for x in self.top_scores]

    def write_top_score(self):
        """ Write user score to rating """
        f = open('scores.json', 'w')
        scores = json.loads(f.read())
        scores.append({'name': self.player_name, 'score': self.score})
        f.write(json.dumps(scores))
        f.close()
