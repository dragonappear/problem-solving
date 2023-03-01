# https://www.acmicpc.net/problem/13460
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


def dfs(rr, rc, br, bc, cnt):
    global mn

    if cnt >= 10:
        return

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

        nrr, nrc, nbr, nbc = rr, rc, br, bc

        while board[nbr+dr][nbc+dc] == '.':
            nbr += dr
            nbc += dc

        if board[nbr+dr][nbc+dc] == 'O':
            continue

        while board[nrr+dr][nrc+dc] == '.':
            nrr += dr
            nrc += dc

        if board[nrr+dr][nrc+dc] == 'O':
            mn = min(mn, cnt+1)
            return

        if (nrr, nrc) == (nbr, nbc):
            if dr == 1:
                if(rr > br):
                    nbr -= 1
                else:
                    nrr -= 1
            elif dr == -1:
                if(rr > br):
                    nrr += 1
                else:
                    nbr += 1
            elif dc == 1:
                if(rc > bc):
                    nbc -= 1
                else:
                    nrc -= 1
            elif dc == -1:
                if(rc > bc):
                    nrc += 1
                else:
                    nbc += 1

        if vis[nrr][nrc][nbr][nbc]:
            continue

        vis[nrr][nrc][nbr][nbc] = True
        dfs(nrr, nrc, nbr, nbc, cnt+1)
        vis[nrr][nrc][nbr][nbc] = False


N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
mn = float('inf')

for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            br, bc = (i, j)
            board[i][j] = '.'
        elif board[i][j] == 'R':
            rr, rc = (i, j)
            board[i][j] = '.'

# vis[rr][rc][br][bc]: (rr,rc)(br,bc) 상태 방문 확인
vis = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
vis[rr][rc][br][bc] = True
dfs(rr, rc, br, bc, 0)

print(mn if mn != float('inf') else -1)
