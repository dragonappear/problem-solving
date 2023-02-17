# https://www.acmicpc.net/problem/4386
from sys import stdin
from math import sqrt
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


def get_dist(ir, ic, jr, jc):
    return round(sqrt(abs(ir-jr)*abs(ir-jr) + abs(ic-jc)*abs(ic-jc)), 2)


N = int(input())
parent = [i for i in range(N)]
stars = [list(map(float, input().split())) for _ in range(N)]
edges = []
for i in range(len(stars)-1):
    for j in range(i+1, len(stars)):
        ir, ic = stars[i]
        jr, jc = stars[j]
        edges.append((get_dist(ir, ic, jr, jc), i, j))

edges.sort()
ans = v = 0
for edge in edges:
    cost, a, b = edge
    if find(a) == find(b):
        continue
    union(a, b)
    v += 1
    ans += cost
    if v == N-1:
        break
print(ans)
