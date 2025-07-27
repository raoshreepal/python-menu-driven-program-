import numpy as np

class Marks:
    def __init__(self, scores):
        self.scores = np.array(scores)

    def average(self):
        total = 0
        for s in self.scores:
            total += s
        return total / len(self.scores)

class Ranking(Marks):
    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        else:
            return "C"

r = Ranking([95, 88, 92])
print("Average:", r.average(), "Grade:", r.grade())
