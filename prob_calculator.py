import copy
import random


class Hat:
    def __init__(self, **args):
        self.contents = list()

        for i, j in args.items():
            for k in range(j):
                self.contents.append(i)

    def draw(self, noOfBallsDrawn):
        if noOfBallsDrawn > len(self.contents):
            return self.contents

        ballsDrawn = list()

        for i in range(noOfBallsDrawn):
            rand_int = random.randrange(len(self.contents))
            ballsDrawn.append(self.contents[rand_int])
            self.contents.pop(rand_int)

        return ballsDrawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected = []

    for i, j in expected_balls.items():
        for k in range(j):
            expected.append(i)

    M = 0

    contentsCopy = copy.deepcopy(hat.contents)

    for i in range(num_experiments):
        drawn = hat.draw(num_balls_drawn)
        hat.contents = copy.deepcopy(contentsCopy)
        count = 0
        for i in expected:
            for j in drawn:
                if i == j:
                    count += 1
                    drawn.pop(drawn.index(j))
                    break
            if count == len(expected):
                M += 1

    return M / num_experiments
