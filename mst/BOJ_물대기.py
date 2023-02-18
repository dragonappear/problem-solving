# https://www.acmicpc.net/problem/1368
from sys import stdin
input = stdin.readline


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    x = find(a)
    y = find(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N = int(input())
edges = set()
for i in range(N):
    cost = int(input())
    edges.add((cost, i, N))

P = [list(map(int, input().strip().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        edges.add((P[i][j], i, j))

edges = sorted(list(edges))
parent = [i for i in range(N+1)]

ans = v = 0
for edge in edges:
    cost, a, b = edge
    if find(a) == find(b):
        continue
    union(a, b)
    ans += cost
    v += 1
    if v == N:
        break
print(ans)
