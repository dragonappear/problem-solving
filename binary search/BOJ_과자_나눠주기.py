# https://www.acmicpc.net/problem/16401
from sys import stdin
from bisect import bisect_left
input = stdin.readline

M, N = map(int, input().split())  # 조카,과자
L = list(map(int, input().split()))
L.sort()

lt, rt = 1, L[-1]

while lt <= rt:
    mid = (lt+rt)//2
    cnt = rmd = 0

    for n in L:
        cnt += (n // mid)
        rmd += (n % mid)
        if rmd == mid:
            cnt += 1
            rmd = 0

    if cnt >= M:
        lt = mid+1
    else:
        rt = mid-1

print(lt-1)


"""
10%7 = 3
10%7 = 3
15%7 = 1

"""
