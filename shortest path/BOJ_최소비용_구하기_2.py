# https://www.acmicpc.net/problem/11779
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
input = stdin.readline

N = int(input())
M = int(input())
graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().strip().split())

    graph[u].append((v, w))

S, E = map(int, input().split())

heap = [(0, S, S)]
dist = defaultdict(int)
prev = [i for i in range(N+1)]

while heap:
    d, u, p = heappop(heap)
    if u not in dist:
        dist[u] = d
        prev[u] = p
        for v, w in graph[u]:
            heappush(heap, (d+w, v, u))

print(dist[E])
tmp, rst = E, []
while prev[tmp] != tmp:
    rst.append(tmp)
    tmp = prev[tmp]
rst.append(prev[tmp])

print(len(rst))
print(*reversed(rst))
