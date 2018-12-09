from itertools import cycle
from collections import deque


def play(players, marbles):
    score = {}
    for p in range(1, players + 1):
        score[p] = 0

    players = cycle(range(1, players + 1))
    circle = deque([0])
    
    for marble in range(1, marbles + 1):
        player = next(players)
 
        if marble % 23 == 0:
            circle.rotate(7)
            score[player] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    highscore = max(score.values())
    return highscore


# 410 players; last marble is worth 72059 points
print("highscore is %d" % play(410, 72059))
print("highscore after 100x the number of marbles is %d" % play(410, 72059 * 100))
