# https://www.acmicpc.net/problem/20183
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
input = stdin.readline
INF = float('inf')


def dijk(limit):
    dist = [INF] * (N + 1)
    dist[A] = 0
    heap = [(0, A)]

    while heap:
        d, u = heappop(heap)

        if dist[u] < d:
            continue

        for v, w in graph[u]:
            if dist[v] <= d+w or w > limit or d+w > C:
                continue

            dist[v] = d+w

            if v == B and dist[v] <= C:
                return True

            heappush(heap, (d+w, v))

    return False


N, M, A, B, C = map(int, input().split())
graph = defaultdict(list)
cost = set()
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    cost.add(w)

cost = sorted(cost)

lt, rt = 0, len(cost)-1
ans = -1
while lt <= rt:
    mid = (lt+rt)//2

    if dijk(cost[mid]):
        rt = mid-1
        ans = cost[mid]
    else:
        lt = mid+1

print(ans)
