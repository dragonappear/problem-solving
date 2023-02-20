# https://www.acmicpc.net/problem/11404
from sys import stdin
input = stdin.readline

V = int(input())
E = int(input())
d = [[float('inf')] * V for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = min(d[a-1][b-1], c)

for i in range(V):
    d[i][i] = 0

for k in range(V):
    for i in range(V):
        for j in range(V):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

for a in d:
    for n in a:
        print(n if n != float('inf') else 0, end=' ')
    print()
