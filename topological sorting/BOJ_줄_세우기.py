# https://www.acmicpc.net/problem/2252
from sys import stdin
from collections import deque, defaultdict
input = stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)
idg = [0]*(N+1)
for _ in range(M):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    idg[v] += 1

q = deque([i for i in range(1, N+1) if idg[i] == 0])

rst = []
while q:
    u = q.popleft()
    rst.append(u)
    for v in graph[u]:
        idg[v] -= 1
        if idg[v] == 0:
            q.append(v)

print(*rst)
