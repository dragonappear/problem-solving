# https://www.acmicpc.net/problem/1018
from sys import stdin
input = stdin.readline


def dfs(idx, cnt, color):

    global mn

    if (idx-r) == 8:
        mn = min(mn, cnt)
        return

    if (idx-r) % 2 == 0:
        tmp = 0

        for i in range(c, c+8):
            if i % 2 == 0:
                if board[idx][i] != color:
                    tmp += 1
            else:
                if board[idx][i] == color:
                    tmp += 1

        dfs(idx+1, cnt+tmp, color)
    else:
        tmp = 0

        for i in range(c, c+8):
            if i % 2 == 0:
                if board[idx][i] == color:
                    tmp += 1
            else:
                if board[idx][i] != color:
                    tmp += 1

        dfs(idx+1, cnt+tmp, color)


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
mn = float('inf')

for r, c in [(i, j) for i in range(N-7) for j in range(M-7)]:
    dfs(r, 0, 'W')
    dfs(r, 0, 'B')

print(mn)
