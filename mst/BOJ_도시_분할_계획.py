# https://www.acmicpc.net/problem/1647
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(int(1e9))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    x = find(a)
    y = find(b)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

rst = cnt = 0
for edge in edges:
    c, a, b = edge
    if find(a) == find(b):
        continue
    union(a, b)
    rst += c
    cnt += 1
    if cnt == N-2:
        break

print(rst)
