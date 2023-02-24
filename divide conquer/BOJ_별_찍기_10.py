# https://www.acmicpc.net/problem/2447
from sys import stdin
input = stdin.readline


def out(r, c):
    for i in range(3):
        stars[r][c+i] = '*'
        stars[r+2][c+i] = '*'

    stars[r+1][c] = '*'
    stars[r+1][c+2] = '*'


def solve(r, c, n):
    if n == 3:
        out(r, c)
        return

    t = (n//3)
    for i in range(3):
        for j in range(3):
            if (i, j) == (1, 1):
                continue
            solve(r+i*t, c+j*t, t)


N = int(input())
stars = [[' ' for _ in range(N)] for _ in range(N)]

solve(0, 0, N)
for i in stars:
    print(''.join(i))
