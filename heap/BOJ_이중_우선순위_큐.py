# https://www.acmicpc.net/problem/7662
from heapq import heappush, heappop
from sys import stdin, stdout
input, write = stdin.readline, stdout.write

result = []
for T in range(int(input())):

    k = int(input())
    vis = [False] * k
    minh, maxh = [], []

    for i in range(k):
        s = input().split()
        cmd, value = s[0], int(s[1])

        if cmd == 'I':
            heappush(minh, (value, i))
            heappush(maxh, (-value, i))
            vis[i] = True

        elif value == 1:
            while maxh and not vis[maxh[0][1]]:  # 동기화 부분
                heappop(maxh)
            if maxh:
                vis[maxh[0][1]] = False
                heappop(maxh)
        else:
            while minh and not vis[minh[0][1]]:  # 동기화 부분
                heappop(minh)
            if minh:
                vis[minh[0][1]] = False
                heappop(minh)

    while minh and not vis[minh[0][1]]:  # 동기화 부분
        heappop(minh)

    while maxh and not vis[maxh[0][1]]:  # 동기화 부분
        heappop(maxh)

    if maxh and minh:
        write(str(-maxh[0][0]) + " " + str(minh[0][0])+"\n")
    else:
        write("EMPTY\n")
