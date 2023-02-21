# https://www.acmicpc.net/problem/1956
from sys import stdin
input = stdin.readline
INF = float('inf')

V, E = map(int, input().split())
d = [[INF] * V for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    d[u-1][v-1] = w

for i in range(V):
    d[i][i] = 0

for k in range(V):
    for i in range(V):
        for j in range(V):
            if d[i][j] > d[i][k]+d[k][j]:
                d[i][j] = d[i][k]+d[k][j]

ans = INF
for i in range(V):
    for j in range(i+1, V):
        if d[i][j] != INF and d[j][i] != INF:  # 사이클 발견
            ans = min(ans, d[i][j]+d[j][i])

print(ans if ans != INF else -1)
