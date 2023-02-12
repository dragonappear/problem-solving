# https://www.acmicpc.net/problem/16985
from sys import stdin, setrecursionlimit
from collections import defaultdict, deque
input = stdin.readline
setrecursionlimit(int(1e9))


def bfs():

    for i in range(1, V+1):
        if t[i]:
            continue
        q = deque([i])
        t[i] = 1
        while q:
            u = q.popleft()
            for v in graph[u]:
                if t[u] == t[v]:
                    return False
                if t[v] and t[u] != t[v]:
                    continue

                t[v] = -t[u]
                q.append(v)

    return True


def dfs(u):
    for v in graph[u]:
        if t[v]:
            if t[v] == t[u]:
                return False
            continue
        else:
            t[v] = -t[u]
            rst = dfs(v)
            if not rst:
                return False
    return True


for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    t = [0] * (V + 1)
    escape = False
    for i in range(1, V+1):
        if t[i]:
            continue
        t[i] = 1
        if not dfs(i):
            escape = True
            break
    if escape:
        print("NO")
    else:
        print("YES")
