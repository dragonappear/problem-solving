# https://www.acmicpc.net/problem/13460
from sys import stdin, stdout
from collections import deque
input, write = stdin.readline, stdout.write


def bfs():
    dist[red[0]][red[1]][blue[0]][blue[1]] = 0
    q = deque([(red[0], red[1], blue[0], blue[1])])

    while q:
        rr, rc, br, bc = q.popleft()
        d = dist[rr][rc][br][bc]

        if d >= 10:
            return -1

        # 4방향으로 기울이기
        for dr, dc in dr_dc:
            nrr, nrc, nbr, nbc = rr, rc, br, bc

            # Blue 이동 벽만날때 or 구멍 만날때까지
            while board[nbr+dr][nbc+dc] == '.':
                nbr += dr
                nbc += dc

            # Blue가 구멍이면 continue
            if board[nbr+dr][nbc+dc] == 'O':
                continue

            # Red 이동 벽만날때 or 구멍 만날때까지
            while board[nrr+dr][nrc+dc] == '.':
                nrr += dr
                nrc += dc

            # Red가 구멍이면 종료
            if board[nrr+dr][nrc+dc] == 'O':
                return d+1

            # 겹쳐진 경우 늦게 출발한 구슬 한칸 뒤로 이동
            if (nrr, nrc) == (nbr, nbc):
                if dc == 1:
                    if rc < bc:
                        nrc -= 1
                    else:
                        nbc -= 1
                elif dr == 1:
                    if rr < br:
                        nrr -= 1
                    else:
                        nbr -= 1
                elif dc == -1:
                    if rc > bc:
                        nrc += 1
                    else:
                        nbc += 1
                else:
                    if rr > br:
                        nrr += 1
                    else:
                        nbr += 1

            if dist[nrr][nrc][nbr][nbc] >= 0:
                continue
            dist[nrr][nrc][nbr][nbc] = d + 1
            q.append((nrr, nrc, nbr, nbc))

    return -1


N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
# dist[a][b][c][d] : 빨간 구슬이 (a, b)이고 파란 구슬이 (c, d)에 위치한 상황에 도달하기 위한 동작의 횟수
dist = [[[[-1]*11 for _ in range(11)] for _ in range(11)] for _ in range(11)]
dr_dc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            blue = (i, j)
            board[i][j] = '.'
        elif board[i][j] == 'R':
            red = (i, j)
            board[i][j] = '.'

print(bfs())

"""
빨간 구슬과 파란 구슬의 좌표를 가지고 4차원에서 BFS를 돌리면 된다. O(N^2M^2)에 동작한다.
최대 10번이라는 제한이 있기 때문에 O(4^10)의 백트래킹으로도 통과가 가능하다.

def dfs(rr, rc, br, bc, cnt):
    global mn

    if cnt >= 10:
        return

    for dr, dc in dr_dc:

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
# vis[rr][rc][br][bc]: (rr,rc)(br,bc) 상태 방문 확인
vis = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            br, bc = (i, j)
            board[i][j] = '.'
        elif board[i][j] == 'R':
            rr, rc = (i, j)
            board[i][j] = '.'

vis[rr][rc][br][bc] = True
dr_dc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
mn = float('inf')

dfs(rr, rc, br, bc, 0)
print(mn if mn != float('inf') else -1)
"""
