# https://www.acmicpc.net/problem/20438
from sys import stdin
input = stdin.readline

N, K, Q, M = map(int, input().split())
sleep = set(map(int, input().split()))
query = list(map(int, input().split()))

vis = [False] * (N+3)
for q in query:
    if q in sleep:
        continue

    for s in range(q, N+3, q):
        if s in sleep:
            continue
        vis[s] = True

psum = [0] * (N+3)
for i in range(3, N+3):
    psum[i] = psum[i-1]
    if not vis[i]:
        psum[i] += 1

for _ in range(M):
    S, E = map(int, input().split())
    print(psum[E]-psum[S-1])
