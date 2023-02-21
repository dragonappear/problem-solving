# https://www.acmicpc.net/problem/14938
from sys import stdin
input = stdin.readline
INF = float('inf')

N, M, R = map(int, input().split())
ITEMS = list(map(int, input().split()))

d = [[INF]*N for _ in range(N)]

for _ in range(R):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = min(d[a-1][b-1], c)
    d[b-1][a-1] = min(d[a-1][b-1], c)

for i in range(N):
    d[i][i] = 0


for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][j] > d[i][k]+d[k][j]:
                d[i][j] = d[i][k]+d[k][j]

ans = -1
for i in range(N):
    cnt = 0
    for j in range(N):
        if d[i][j] > M:
            continue
        cnt += ITEMS[j]
    ans = max(ans, cnt)

print(ans)
