# https://www.acmicpc.net/problem/11780
from sys import stdin
input = stdin.readline
INF = float('inf')

N = int(input())
d = [[INF] * (N+1) for _ in range(N+1)]
nxt = [[-1] * (N+1) for _ in range(N+1)]

for _ in range(int(input())):
    u, v, w = map(int, input().split())
    if d[u][v] > w:
        d[u][v] = w
        nxt[u][v] = v

for i in range(1, N+1):
    d[i][i] = 0
    nxt[i][i] = i

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if d[i][j] > d[i][k]+d[k][j]:
                d[i][j] = d[i][k]+d[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(1, N+1):
    for j in range(1, N+1):
        print(d[i][j] if d[i][j] != INF else 0, end=' ')
    print()

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j or d[i][j] == INF:
            print(0)
            continue

        path = []
        st = i
        while st != j:
            path.append(st)
            st = nxt[st][j]
        path.append(j)
        print(len(path), *path)
