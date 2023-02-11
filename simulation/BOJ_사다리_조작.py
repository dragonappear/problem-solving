# https://www.acmicpc.net/problem/15684
from sys import stdin
from itertools import combinations
input = stdin.readline


def check():
    for j in range(N):
        col = j  # 세로선
        for i in range(H):
            if board[i][col]:
                col += 1
            elif col > 0 and board[i][col-1]:
                col -= 1
        if col != j:
            return False
    return True


N, M, H = map(int, input().split())
board = [[False]*N for _ in range(H)]

for _ in range(M):
    A, B = map(int, input().split())
    board[A-1][B-1] = True

for i in range(4):
    for combi in combinations([(i, j) for i in range(H) for j in range(N-1) if not board[i][j]], i):
        for a, b in combi:
            board[a][b] = True
        if check():
            print(i)
            exit()
        for a, b in combi:
            board[a][b] = False

print(-1)
