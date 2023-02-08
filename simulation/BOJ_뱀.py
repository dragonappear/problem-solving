# https://www.acmicpc.net/problem/3190
from sys import stdin, stdout
from collections import deque
input, write = stdin.readline, stdout.write

N = int(input())
board = [[0]*N for _ in range(N)]  # 2: 사과 , 1: 뱀 , 0: 빈 칸
dir = [[0]*N for _ in range(N)]  # 각 칸의 방향
for _ in range(int(input())):
    a, b = map(int, input().split())
    board[a-1][b-1] = 2

actions = deque()
for i in range(int(input())):
    a, b = input().split()
    actions.append((int(a), b))

sr, sc, er, ec = 0, 0, 0, 0
time = 0
dr_dc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0
board[sr][sc] = board[er][ec] = 1
dir[sr][sc] = 0

while True:
    time += 1

    nsr, nsc = sr+dr_dc[d][0], sc+dr_dc[d][1]
    if not(0 <= nsr < N) or not(0 <= nsc < N) or board[nsr][nsc] == 1:  # 게임 종료
        break

    if board[nsr][nsc] != 2:
        board[er][ec] = 0
        er, ec = er+dr_dc[dir[er][ec]][0], ec+dr_dc[dir[er][ec]][1]

    board[nsr][nsc] = 1
    dir[nsr][nsc] = d
    sr, sc = nsr, nsc

    if actions and time == actions[0][0]:
        t, c = actions.popleft()

        if c == "D":
            d = (d+1) % 4
        else:
            d = (d-1) % 4
        dir[sr][sc] = d

print(time)
