# https://www.acmicpc.net/problem/11437
from sys import stdin, setrecursionlimit
from collections import defaultdict
input = stdin.readline
setrecursionlimit(int(1e5))


def lca(a, b):  # a와 b의 최소 공통 조상을 찾는 함수
    # 1.깊이가 동일하도록 설정
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = p[a]
        else:
            b = p[b]

    # 2.노드가 같아질떄까지 반복
    while a != b:
        a = p[a]
        b = p[b]

    return a


def dfs(u, depth):
    for v in graph[u]:
        if vis[v]:
            continue
        p[v] = u
        vis[v] = True
        d[v] = depth+1
        dfs(v, depth+1)


N = int(input())
p = [0]*(N+1)  # 부모
d = [0]*(N+1)  # depth
vis = [False]*(N+1)  # 방문 체크
graph = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

vis[1] = True
d[1] = 0
dfs(1, 0)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lca(a, b))


"""
O(NM)
"""
