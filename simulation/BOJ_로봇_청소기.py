# https://www.acmicpc.net/problem/14503
from sys import stdin, stdout
input, write = stdin.readline, stdout.write

N, M = map(int, input().split())
R, C, D = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
dr_dc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ans = 0
while True:

    if board[R][C] == 0:  # 청소하지 않는 칸
        ans += 1
    board[R][C] = -1  # 청소

    clean = False
    for i in range(4):  # 왼쪽 공간 탐색
        D = (D+3) % 4  # 왼쪽 회전
        if board[R+dr_dc[D][0]][C+dr_dc[D][1]] == 0:  # 청소안한곳 확인
            R += dr_dc[D][0]
            C += dr_dc[D][1]
            clean = True
            break

    if clean:
        continue

    if board[R-dr_dc[D][0]][C-dr_dc[D][1]] == 1:  # 후진 공간 벽 체크
        break

    # 후진
    R -= dr_dc[D][0]
    C -= dr_dc[D][1]

print(ans)
