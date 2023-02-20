# https://www.acmicpc.net/problem/11657
from sys import stdin
input = stdin.readline
INF = float('inf')


def bf():
    dist[1] = 0  # 시작 노드에 대해서 초기화
    for i in range(N):  # 전체 N번의 라운드를 반복
        for u, v, cost in edges:  # 매 반복마다 모든 간선을 확인
            if dist[u] != INF and dist[v] > dist[u] + cost:  # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                dist[v] = dist[u] + cost
                if i == N-1:  # N번째 라운드에서 값이 갱신된다면 음수 순환이 존재
                    return True
    return False


N, M = map(int, input().split())
edges = []
dist = [INF] * (N+1)

for _ in range(M):
    u, v, cost = map(int, input().split())
    edges.append((u, v, cost))

negative_cycle = bf()

if negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
