# https://www.acmicpc.net/problem/1197
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(int(1e9))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges = []

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()


result = 0
for edge in edges:
    c, a, b = edge
    if find(a) == find(b):  # 같은 그룹에 소속되었으면 continue
        continue
    union(a, b)
    result += c

print(result)
