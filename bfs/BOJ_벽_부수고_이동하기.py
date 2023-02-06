# https://www.acmicpc.net/problem/2606
from sys import stdin, stdout
from collections import deque
input, write = stdin.readline, stdout.write


def solve():
    dist = [[[0]*M for _ in range(N)] for _ in range(2)]
    dist[0][0][0] = dist[1][0][0] = 1
    q = deque([(0, 0, 0)])

    while q:
        r, c, broken = q.popleft()

        if r == N-1 and c == M-1:
            return dist[broken][r][c]

        for dr, dc in dr_dc:
            nr, nc = r+dr, c+dc

            # OOB or 이미 방문한 경우
            if not(0 <= nr < N) or not(0 <= nc < M) or dist[broken][nr][nc] > 0:
                continue
            # 다음칸이 벽인데 깰수없는 경우
            if graph[nr][nc] == 1 and broken == 1:
                continue
            # 다음칸이 벽인데 깰수있는데 이미 방문한 경우
            if graph[nr][nc] == 1 and broken == 0 and dist[1][nr][nc] > 0:
                continue

            if graph[nr][nc] == 1 and broken == 0:  # 부시고 방문
                dist[1][nr][nc] = dist[0][r][c]+1
                q.append((nr, nc, 1))
            else:  # 그대로 방문
                dist[broken][nr][nc] = dist[broken][r][c]+1
                q.append((nr, nc, broken))

    return -1


N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
dr_dc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
print(solve())
