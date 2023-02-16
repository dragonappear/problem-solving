# https://www.acmicpc.net/problem/1922
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(int(1e9))


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
M = int(input())
parent = [i for i in range(N+1)]
edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
rst = 0
for i in range(M):
    cost, a, b = edges[i]
    if find(a) == find(b):
        continue
    union(a, b)
    rst += cost

print(rst)
