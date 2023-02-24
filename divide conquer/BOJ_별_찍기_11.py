# https://www.acmicpc.net/problem/2448
from sys import stdin
input = stdin.readline


def out(r, c):
    board[r][c] = board[r+2][c] = '*'
    board[r+1][c-1] = board[r+1][c+1] = '*'

    for i in range(1, 3):
        board[r+2][c+i] = board[r+2][c-i] = '*'


def solve(r, c, n):
    if n == 3:
        out(r, c)
        return

    t = n//2
    solve(r, c, t)
    solve(r+t, c-t, t)
    solve(r+t, c+t, t)


N = int(input())
board = [[' ' for _ in range(2*N-1)] for _ in range(N)]

solve(0, N-1, N)

for i in board:
    print(''.join(i))
