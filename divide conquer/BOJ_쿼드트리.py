# https://www.acmicpc.net/problem/1992
from sys import stdin
input = stdin.readline


def check(r, c, n):
    a = board[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if a != board[i][j]:
                return False
    return True


def solve(r, c, n):

    if check(r, c, n):
        return str(board[r][c])

    half = (n >> 1)

    ul = solve(r, c, half)
    ur = solve(r, c+half, half)
    bl = solve(r+half, c, half)
    br = solve(r+half, c+half, half)

    return "(" + ul+ur+bl+br + ")"


N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
print(solve(0, 0, N))
