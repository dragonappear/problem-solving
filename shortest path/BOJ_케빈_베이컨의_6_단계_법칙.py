# https://www.acmicpc.net/problem/1389
from sys import stdin
input = stdin.readline
INF = float('inf')

N, M = map(int, input().split())
d = [[INF] * (N) for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    d[u-1][v-1] = d[v-1][u-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][j] > d[i][k]+d[k][j]:
                d[i][j] = d[i][k]+d[k][j]

for i in range(N):
    d[i][i] = 0

mn = INF
idx = -1
for i in range(N):
    s = sum(d[i])
    if mn > s:
        idx = i
        mn = s

print(idx+1)
