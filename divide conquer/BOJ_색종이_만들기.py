# https://www.acmicpc.net/problem/2630
from sys import stdin
input = stdin.readline


def check(i, j, n):
    a = board[i][j]
    for r in range(i, i+n):
        for c in range(j, j+n):
            if a != board[r][c]:
                return False
    return True


def solve(r, c, n):
    global blue, white

    if n == 0:
        return

    if check(r, c, n):
        if board[r][c]:
            blue += 1
        else:
            white += 1
        return

    half = n//2
    solve(r, c, half)
    solve(r, c+half, half)
    solve(r+half, c, half)
    solve(r+half, c+half, half)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
white = blue = 0

solve(0, 0, N)
print(white)
print(blue)
