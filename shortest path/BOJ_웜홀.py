# https://www.acmicpc.net/problem/1865
from sys import stdin
input = stdin.readline
INF = int(1e9)


def bf():
    dist[1] = 0

    for i in range(N):
        for u, v, cost in edges:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                if i == N-1:
                    return True
    return False


for _ in range(int(input())):
    N, M, W = map(int, input().split())
    dist = [INF]*(N+1)
    edges = []

    for _ in range(M):
        u, v, cost = map(int, input().split())
        edges.append((u, v, cost))
        edges.append((v, u, cost))

    for _ in range(W):
        u, v, cost = map(int, input().split())
        edges.append((u, v, -cost))

    print("YES" if bf() else "NO")
