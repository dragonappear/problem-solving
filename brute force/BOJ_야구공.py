# https://www.acmicpc.net/problem/17281
from sys import stdin
from itertools import permutations
input = stdin.readline


def game(line):
    player = score = 0
    for inning in innings:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if inning[line[player]] == 0:
                out += 1
            elif inning[line[player]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif inning[line[player]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif inning[line[player]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif inning[line[player]] == 4:
                score += (1 + b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 0

            player = (player + 1) % 9

    return score


N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]

mx = -1
for p in permutations(range(1, 9), 8):
    p = list(p)
    p.insert(3, 0)
    rst = game(p)
    if mx < rst:
        mx = rst

print(mx)
