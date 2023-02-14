# https://www.acmicpc.net/problem/21939
from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

N = int(input())
pbms = [list(map(int, input().split())) for _ in range(N)]

vis = [[False] * 101 for _ in range(100_001)]
maxh, minh = [], []

for pb in pbms:
    heappush(maxh, (-pb[1], -pb[0]))
    heappush(minh, (pb[1], pb[0]))
    vis[pb[0]][pb[1]] = True

for _ in range(int(input())):
    x = input().split()
    cmd = x[0]

    if cmd == "add":  # log(n)
        p, l = int(x[1]), int(x[2])
        heappush(maxh, (-l, -p))
        heappush(minh, (l, p))
        vis[p][l] = True

    elif cmd == "recommend":  # log(1)
        if int(x[1]) > 0:
            while maxh and not vis[-maxh[0][1]][-maxh[0][0]]:
                heappop(maxh)
            print(-maxh[0][1])
        else:
            while minh and not vis[minh[0][1]][minh[0][0]]:
                heappop(minh)
            print(minh[0][1])

    elif cmd == "solved":
        p = int(x[1])
        vis[p] = [False]*(101)
