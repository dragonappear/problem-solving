# https://www.acmicpc.net/problem/2458
from sys import stdin
input = stdin.readline
INF = 0

N, M = map(int, input().split())
dist = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    dist[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][k] & dist[k][j]:
                dist[i][j] = 1

ans = 0
for i in range(N):
    cnt = 0
    cnt += int(sum(1 for j in range(N)
               if dist[i][j] > 0 and dist[i][j] != 0))
    cnt += int(sum(1 for j in range(N)
               if dist[j][i] > 0 and dist[j][i] != 0))
    if cnt == N-1:
        ans += 1

print(ans)
