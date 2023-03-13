# https://www.acmicpc.net/problem/17143
from sys import stdin
input = stdin.readline


def move():

    def _move():
        s, d, z = board[i][j]
        cnt = s
        r, c = i, j
        while cnt:
            cnt -= 1
            dr, dc = dr_dc[d]
            nr, nc = r+dr, c+dc
            if not(0 <= nr < R) or not(0 <= nc < C):
                if d % 2 == 0:
                    d += 1
                else:
                    d -= 1
                dr, dc = dr_dc[d]
                r, c = r+dr, c+dc
            else:
                r, c = nr, nc

        if tmp[r][c]:
            if tmp[r][c][2] < z:
                tmp[r][c] = (s, d, z)
        else:
            tmp[r][c] = (s, d, z)

    tmp = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] == 0:
                continue
            _move()

    for i in range(R):
        for j in range(C):
            board[i][j] = tmp[i][j]


def catch(col):
    global ans

    for i in range(R):
        if board[i][col]:
            ans += board[i][col][-1]
            board[i][col] = 0
            return


R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]
dr_dc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1] = (s, d-1, z)


ans = 0
for i in range(0, C):
    catch(i)
    move()

print(ans)
