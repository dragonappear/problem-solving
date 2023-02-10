# https://www.acmicpc.net/problem/11725
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict, deque
input, write = stdin.readline, stdout.write
setrecursionlimit(10**9)


def recursive(u):
    for v in adj[u]:
        if p[u] == v:  # 부모노드이면 pass
            continue
        p[v] = u  # 부모노드 설정
        recursive(v)


def iterative():
    stack = [1]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if p[u] == v:  # 부모노드이면 pass
                continue
            p[v] = u  # 부모노드 설정
            stack.append(v)


def bfs():
    q = deque([1])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if p[u] == v:  # 부모노드이면 pass
                continue
            p[v] = u
            q.append(v)


N = int(input())
adj = defaultdict(list)
p = [-1]*(N+1)
for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

p[1] = 0
# recursive(1)
# iterative()
bfs()
for i in range(2, N+1):
    print(p[i])
