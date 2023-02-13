# https://www.acmicpc.net/problem/4803
from sys import stdin
from collections import defaultdict
input = stdin.readline


def check(u):
    for v in graph[u]:
        if vis[v]:
            if parent[u] != v:
                return False
            continue
        parent[v] = u
        vis[v] = True
        if not check(v):
            return False
    return True


t = 1
while True:
    N, M = map(int, input().split())

    if (N, M) == (0, 0):
        break

    graph = defaultdict(list)
    vis = [False]*(N+1)  # 방문체크
    parent = [0]*(N+1)  # 부모노드

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    ans = 0
    for i in range(1, N+1):
        if vis[i]:
            continue
        vis[i] = True
        if check(i):
            ans += 1

    if ans == 0:
        print(f'Case {t}: No trees.')
    elif ans == 1:
        print(f'Case {t}: There is one tree.')
    else:
        print(f'Case {t}: A forest of {ans} trees.')

    t += 1
