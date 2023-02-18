# https://www.acmicpc.net/problem/9372
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


for _ in range(int(input())):
    N, M = map(int, input().split())

    parent = [i for i in range(N+1)]
    edges = []

    for _ in range(M):
        u, v = map(int, input().split())
        edges.append((1, u, v))

    edges.sort()
    ans = cnt = 0
    for edge in edges:
        cost, a, b = edge
        if find(a) == find(b):
            continue
        union(a, b)
        ans += cost
        if cnt == N-1:
            break

    print(ans)
