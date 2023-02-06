# https://www.acmicpc.net/problem/2606
from sys import stdin, stdout
from collections import defaultdict, deque
input, write = stdin.readline, stdout.write

"""
BFS
"""


def bfs():
    visit = [False] * (N+1)
    q = deque([1])
    visit[1] = True
    cnt = 0
    while q:
        u = q.popleft()
        for v in graph[u]:
            if visit[v]:
                continue
            visit[v] = True
            cnt += 1
            q.append(v)
    return cnt


"""
DFS
"""


def dfs(u):
    global cnt

    for v in graph[u]:
        if visit[v]:
            continue
        visit[v] = True
        cnt += 1
        dfs(v)


N = int(input())
M = int(input())
graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs())

cnt = 0
visit = [False] * (N+1)
visit[1] = True
dfs(1)
print(cnt)
