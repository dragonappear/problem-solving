# https://www.acmicpc.net/problem/10473
from sys import stdin
from math import sqrt
from collections import defaultdict
from heapq import heappush, heappop
input = stdin.readline
INF = float('inf')


def get_cannon(fx, fy, tx, ty):
    d = sqrt(abs(fx-tx)**2 + abs(fy-ty)**2)
    return 2.0 + abs(d-50) / 5.0


def get_walk(x, y):
    return sqrt(abs(SX-x)**2 + abs(SY-y)**2) / 5.0


SX, SY = map(float, input().split())
EX, EY = map(float, input().split())
N = int(input())
pos = [0]
graph = defaultdict(list)

for i in range(1, N+1):
    x, y = map(float, input().split())
    graph[0].append((i, get_walk(x, y)))
    graph[i].append((N+1, get_cannon(x, y, EX, EY)))
    pos.append((x, y))

graph[0].append((N+1, get_walk(EX, EY)))

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            continue
        fx, fy = pos[i]
        tx, ty = pos[j]
        d = get_cannon(fx, fy, tx, ty)
        graph[i].append((j, d))
        graph[j].append((i, d))

dist = [INF]*(N+2)
dist[0] = 0
heap = [(0, 0)]
while heap:
    d, u = heappop(heap)

    if u == N+1:
        print(round(dist[N+1], 6))
        exit()

    if dist[u] < d:
        continue

    for v, w in graph[u]:
        if dist[v] < d+w:
            continue
        dist[v] = d+w
        heappush(heap, (d+w, v))
