# https://www.acmicpc.net/problem/2263
from sys import stdin, stdout, setrecursionlimit
input, write = stdin.readline, stdout.write
setrecursionlimit(10**9)


def solve(il, ir, pl, pr):

    if il > ir or pl > pr:
        return

    p = post_order[pr]
    print(p, end=' ')

    # 왼쪽
    solve(il, idx[p]-1, pl, pl+(idx[p]-il)-1)
    # 오른쪽
    solve(idx[p]+1, ir, pl+(idx[p]-il), pr-1)


N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
idx = [0] * (N+1)

for i in range(N):
    idx[in_order[i]] = i

solve(0, N-1, 0, N-1)
