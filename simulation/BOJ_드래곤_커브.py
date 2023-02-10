# https://www.acmicpc.net/problem/15685
from sys import stdin, stdout
input, write = stdin.readline, stdout.write

N = int(input())
board = [[0] * 105 for _ in range(105)]
cnt = 0
for _ in range(N):
    X, Y, D, G = map(int, input().strip().split())

    v = []
    v.append(D)
    board[Y][X] = 1

    for _ in range(G):
        vsize = len(v)
    # 세대가 증가할 때마다 기존 세대의 방향(숫자)을 뒤에서부터 1을 더한 방향(숫자)을 추가
    # if D==0
    #   0: 0
    #   1: 0, 1
    #   2: 0, 1, 2, 1
    #   3: 0, 1, 2, 1, 2, 3, 2, 1
        for j in range(vsize-1, -1, -1):
            v.append((v[j]+1) % 4)

    for i in range(len(v)):
        dir = v[i]
        if dir == 0:
            X += 1
        elif dir == 1:
            Y -= 1
        elif dir == 2:
            X -= 1
        elif dir == 3:
            Y += 1

        board[Y][X] = 1

for i in range(100):
    for j in range(100):
        if not board[i][j]:
            continue
        if board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            cnt += 1

print(cnt)
