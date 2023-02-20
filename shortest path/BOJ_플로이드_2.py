# https://www.acmicpc.net/problem/11780
from sys import stdin
input = stdin.readline

MAX = float('inf')
V = int(input())
E = int(input())
d = [[MAX] * (V+1) for _ in range(V+1)]
nxt = [[0] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    d[a][b] = min(d[a][b], c)
    nxt[a][b] = b

for i in range(1, V+1):
    d[i][i] = 0

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if d[i][j] > d[i][k]+d[k][j]:
                d[i][j] = d[i][k]+d[k][j]
                nxt[i][j] = nxt[i][k]


for i in range(1, V+1):
    for j in range(1, V+1):
        print(d[i][j] if d[i][j] != MAX else 0, end=' ')
    print()

for i in range(1, V+1):
    for j in range(1, V+1):
        if d[i][j] == 0 or d[i][j] == MAX:
            print(0)
            continue

        path = []
        st = i
        while st != j:
            path.append(st)
            st = nxt[st][j]
        path.append(j)
        print(len(path), end=' ')
        print(*path)
