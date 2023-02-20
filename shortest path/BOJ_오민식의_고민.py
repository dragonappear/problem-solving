# https://www.acmicpc.net/problem/1219
from sys import stdin
from collections import deque, defaultdict
input = stdin.readline
INF = float('inf')


def bfs(v):
    vis = [False] * N
    q = deque([v])
    vis[v] = True

    while q:
        u = q.popleft()

        if u == END:
            return True

        for v, c in graph[u]:
            if vis[v]:
                continue
            vis[v] = True
            q.append(v)
    return False


def bf():
    dist[START] = -gain[START]

    for i in range(N):
        for u in range(N):
            if dist[u] == INF:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    if i == N-1:  # 음의 사이클 발견
                        if bfs(v):  # 사이클에서 END까지 갈 수 있는 경우
                            print('Gee')
                            return True

    if dist[END] == INF:  # END까지 갈 수 없는 경우
        print('gg')
        return True

    return False


N, START, END, M = map(int, input().split())
dist = [INF] * N

# 그래프 입력
graph = defaultdict(list)
for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

# 수익 초기화
gain = list(map(int, input().split()))

# 방문노드 가중치 초기화
for u in graph:
    for nxt in graph[u]:
        for k in range(N):
            if nxt[0] == k:
                nxt[1] -= gain[k]

if not bf():  # 음의 사이클 발견 X
    print(-dist[END])
