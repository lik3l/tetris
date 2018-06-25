from . import constants as c


class Score:
    def __init__(self):
        self.score = 0
        self.top_scores = list()

    def __str__(self):
        return 'Score: {}'.format(self.score)

    def increase_score(self, count):
        """ Increases score """
        self.score += count ** c.MULTI_LINE_MULTIPLIER * c.LINE_COST

    def get_score(self):
        return 'Your score: {}'.format(self.score)

    def get_score_end(self):
        return 'Your score is: {}'.format(self.score)
