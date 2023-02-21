# https://www.acmicpc.net/problem/13549
from sys import stdin
from collections import deque
input = stdin.readline
INF = float('inf')
LIMIT = 100_010


def teleport(cur):
    st = cur
    if cur == 0:
        return
    while cur < LIMIT and dist[K] == 0:
        if dist[cur] == 0:
            dist[cur] = dist[st]
            q.append(cur)
            if cur == K:
                return
        cur <<= 1


N, K = map(int, input().split())
dist = [0]*(LIMIT)

dist[N] = 1
q = deque([N])
teleport(N)

while q:
    x = q.popleft()
    for n in [x-1, x+1]:
        if not(0 <= n < LIMIT) or dist[n]:
            continue
        dist[n] = dist[x]+1
        q.append(n)
        teleport(n)

print(dist[K]-1)
