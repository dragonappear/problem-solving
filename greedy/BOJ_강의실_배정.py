# https://www.acmicpc.net/problem/11000
from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

N = int(input())

arr = sorted([list(map(int, input().split())) for _ in range(N)])
heap = []

ans = 0
for s, e in arr:
    if not heap:
        ans += 1
    else:
        if heap[0][0] > s:
            ans += 1
        else:
            heappop(heap)

    heappush(heap, (e, s))

print(ans)
