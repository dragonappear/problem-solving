# https://www.acmicpc.net/problem/20183
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
input = stdin.readline
INF = float('inf')


def dijkstra(limit):
    dist = [INF] * (N + 1)
    dist[A] = 0
    heap = [(0, A)]
    while heap:
        c, u = heappop(heap)

        if dist[u] < c:
            continue

        for v, w in graph[u]:
            t = c+w
            if w > limit or t > C:
                continue

            if dist[v] > t:
                dist[v] = t
                heappush(heap, (t, v))

    return dist[B] <= C


N, M, A, B, C = map(int, input().split())
graph = defaultdict(list)
costs = set()
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    costs.add(c)

costs = sorted(costs)
left, right = 0, len(costs)-1
ans = -1
while left <= right:
    mid = (left + right) // 2

    if dijkstra(costs[mid]):
        right = mid-1
        ans = costs[mid]
    else:
        left = mid + 1

print(ans)
