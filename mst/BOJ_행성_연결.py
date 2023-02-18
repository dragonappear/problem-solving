# https://www.acmicpc.net/problem/16398
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(int(1e9))


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
parent = [i for i in range(N)]

graph = [list(map(int, input().split())) for _ in range(N)]
edges = []

for i in range(N-1):
    for j in range(i+1, N):
        edges.append((graph[i][j], i, j))

edges.sort()
ans = cnt = 0

for edge in edges:
    cost, u, v = edge
    if find(u) == find(v):
        continue
    union(u, v)
    ans += cost
    cnt += 1
    if cnt == N-1:
        break
print(ans)
