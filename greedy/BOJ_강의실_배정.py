# https://www.acmicpc.net/problem/2138
from sys import stdin, stdout
from heapq import heappush, heappop
input, write = stdin.readline, stdout.write


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
A.sort()
heap = []
heappush(heap, A[0][1])
for i in range(1, N):
    heappush(heap, A[i][1])
    if heap[0] <= A[i][0]:
        heappop(heap)
print(len(heap))

# 먼저 끝나는 강의의 강의실을 사용해야 한다.
