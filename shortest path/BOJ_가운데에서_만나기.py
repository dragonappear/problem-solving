# https://www.acmicpc.net/problem/21940
from sys import stdin
input = stdin.readline
INF = float('inf')

V, E = map(int, input().split())
d = [[INF]*(V) for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    d[u-1][v-1] = w

K = int(input())
CITY = list(map(int, input().split()))

for i in range(V):
    d[i][i] = 0

for k in range(V):
    for i in range(V):
        for j in range(V):
            if d[i][j] > d[i][k]+d[k][j]:
                d[i][j] = d[i][k]+d[k][j]


idx = []
for i in range(V):
    mx = 0
    for c in CITY:
        mx = max(mx, d[i][c-1]+d[c-1][i])
    idx.append((mx, i))

idx.sort()
mn = idx[0][0]
for a, b in idx:
    if mn < a:
        break
    print(b+1, end=' ')
