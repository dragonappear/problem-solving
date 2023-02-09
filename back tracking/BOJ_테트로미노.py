# https://www.acmicpc.net/problem/14500
from sys import stdin, stdout
input, write = stdin.readline, stdout.write


def solve(r, c, cnt, sum):
    global mx
    if cnt == 4:
        mx = max(mx, sum)
        return

    for dr, dc in dr_dc:
        nr, nc = r+dr, c+dc
        if not(0 <= nr < N) or not(0 <= nc < M) or visit[nr][nc]:
            continue

        sum += board[nr][nc]
        visit[nr][nc] = True
        solve(nr, nc, cnt+1, sum)
        if cnt == 2:
            solve(r, c, cnt+1, sum)
        sum -= board[nr][nc]
        visit[nr][nc] = False


N, M = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
dr_dc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
mx = 0

for i in range(N):
    for j in range(M):
        sum = board[i][j]
        visit[i][j] = True
        solve(i, j, 1, sum)
        visit[i][j] = False
print(mx)

"""
ㅗㅜㅓㅏ를 제외한 모든 테트로미노는
길이가 4인 루트를 찾는 백트래킹으로 얻을 수 있다.
ㅗㅜㅓㅏ는 cnt == 2에서 3번째 정사각형을 뽑은 뒤
현위치인 (cx, cy)를 인자로 다시 보내 찾을 수 있다.
해당 코드는 34-35번째 줄과 같이 구현된다.
"""
