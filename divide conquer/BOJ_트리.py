# https://www.acmicpc.net/problem/4256
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**9)


def solve(il, ir, pl, pr):

    if il > ir or pl > pr:
        return

    p = pre_order[pl]

    # 왼쪽

    solve(il, idx[p]-1, pl+1, pl + (idx[p]-il))

    # 오른쪽
    solve(idx[p]+1, ir, pl+(idx[p]-il)+1, pr)

    print(p, end=' ')


for _ in range(int(input())):
    N = int(input())
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))
    idx = [0] * (N+1)
    for i in range(N):
        idx[in_order[i]] = i

    solve(0, N-1, 0, N-1)
    print()
