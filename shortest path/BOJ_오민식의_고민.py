# https://www.acmicpc.net/problem/1219
from sys import stdin
from collections import deque, defaultdict
input = stdin.readline
INF = int(1e9)


def bfs(v):
    if v == END:
        return True

    vis = [False] * N
    q = deque([v])
    vis[v] = True

    while q:
        u = q.popleft()
        for v in graph[u]:
            if vis[v]:
                continue
            if v == END:
                return True
            vis[v] = True
            q.append(v)

    return False


def bf():
    dist = [INF] * N
    dist[START] = -gain[START]

    for i in range(N):
        for u, v, w in edgs:
            if dist[u] != INF and dist[v] > dist[u]+w:
                dist[v] = dist[u] + w
                if i == N-1:  # 음의 사이클 발견
                    if bfs(v):  # 사이클에서 END까지 갈 수 있는 경우
                        return "Gee"

        if i == N-1 and dist[END] == INF:  # END까지 갈 수 없는 경우
            return "gg"

    return -dist[END]  # 음의 사이클 발견 X


N, START, END, M = map(int, input().split())

graph = defaultdict(list)
edgs = []
for i in range(M):
    u, v, w = map(int, input().split())
    edgs.append([u, v, w])
    graph[u].append(v)

gain = list(map(int, input().split()))

# 가중치 업데이트
# u -> v 로 w 만큼 경비가 필요한데, v로 가면 gain[v]만큼 얻을수 있으므로
# # u -> v 를 w-gain[v]로 업데이트
for edge in edgs:
    edge[2] -= gain[edge[1]]

print(bf())
