# https://www.acmicpc.net/problem/1719
from sys import stdin
input = stdin.readline
INF = float('inf')

N, M = map(int, input().split())
d = [[INF] * N for _ in range(N)]
nxt = [[0] * N for _ in range(N)]


for _ in range(M):
    a, b, w = map(int, input().split())
    d[a-1][b-1] = w
    d[b-1][a-1] = w
    nxt[a-1][b-1] = b
    nxt[b-1][a-1] = a

for i in range(N):
    d[i][i] = 0
    nxt[i][i] = '-'

for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][j] > d[i][k]+d[k][j]:
                d[i][j] = d[i][k]+d[k][j]
                nxt[i][j] = nxt[i][k]


for i in nxt:
    print(*i)
