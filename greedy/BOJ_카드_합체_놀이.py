# https://www.acmicpc.net/problem/15903
from sys import stdin
from heapq import heappush, heappop, heapify
input = stdin.readline


N, M = map(int, input().split())
heap = list(map(int, input().split()))

heapify(heap)

for _ in range(M):
    tmp = heappop(heap)+heappop(heap)

    heappush(heap, tmp)
    heappush(heap, tmp)

print(sum(heap))
