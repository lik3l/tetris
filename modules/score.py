class Score:
    def __init__(self):
        self.score = 0
        self.top_scores = list()

    def __str__(self):
        return 'Score: '.format(self.score)
