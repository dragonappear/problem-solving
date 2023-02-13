# https://www.acmicpc.net/problem/1005
from sys import stdin
from collections import deque, defaultdict
input = stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    graph = defaultdict(list)
    deg = [0]*(N+1)

    time = [0] + list(map(int, input().strip().split()))
    tot = [0]*(N+1)  # i-1번째가 끝날 최대시간

    for _ in range(K):
        u, v = map(int, input().split())
        graph[u].append(v)
        deg[v] += 1

    W = int(input())
    q = deque([i for i in range(1, N+1) if deg[i] == 0])

    while q:
        u = q.popleft()
        for v in graph[u]:
            tot[v] = max(tot[v], time[u]+tot[u])
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    print(tot[W]+time[W])
