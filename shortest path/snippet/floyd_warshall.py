from sys import stdin
input = stdin.readline

# O(V^3)
MAX = float('inf')
V = int(input())
E = int(input())
d = [[MAX] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    d[a][b] = min(d[a][b], c)

for i in range(1, V+1):
    d[i][i] = 0

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])
