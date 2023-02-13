# https://www.acmicpc.net/problem/14567
from sys import stdin
from collections import deque, defaultdict
input = stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)
idg = [0]*(N+1)
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    idg[v] += 1

q = deque([(i, 1) for i in range(1, N+1) if idg[i] == 0])
rst = [0]*(N+1)
while q:
    u, end = q.popleft()
    rst[u] = end
    for v in graph[u]:
        idg[v] -= 1
        if idg[v] == 0:
            q.append((v, end+1))

print(*[rst[i] for i in range(1, N+1)])
