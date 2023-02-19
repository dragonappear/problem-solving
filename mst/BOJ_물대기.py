# https://www.acmicpc.net/problem/1368
from sys import stdin
input = stdin.readline


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    x, y = find(a), find(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N = int(input())
edges = set()
for i in range(N):
    edges.add((int(input()), i, N))

P = [list(map(int, input().strip().split())) for _ in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        if i == j:
            continue
        edges.add((P[i][j], i, j))

edges = sorted(list(edges))
parent = [i for i in range(N+1)]

ans = e = 0
for edge in edges:
    c, a, b = edge
    if find(a) == find(b):
        continue
    union(a, b)
    ans += c
    e += 1
    if e == N:
        break
print(ans)
