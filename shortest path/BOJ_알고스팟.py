# https://www.acmicpc.net/problem/1238
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
input = stdin.readline
INF = float('inf')

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(M)]

dist = [[INF] * N for _ in range(M)]
heap = [(0, 0, 0)]
while heap:
    cnt, r, c = heappop(heap)

    if r == M-1 and c == N-1:
        print(cnt)
        break

    if cnt > dist[r][c]:
        break

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r+dr, c+dc

        if not(0 <= nr < M) or not(0 <= nc < N):
            continue

        if board[nr][nc] == 0:
            if dist[nr][nc] > cnt:
                dist[nr][nc] = cnt
                heappush(heap, (cnt, nr, nc))
        else:
            if dist[nr][nc] > cnt+1:
                dist[nr][nc] = cnt+1
                heappush(heap, (cnt+1, nr, nc))
