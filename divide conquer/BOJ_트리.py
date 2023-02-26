# https://www.acmicpc.net/problem/4256
from sys import stdin
input = stdin.readline


def postorder(il, ir, pl, pr):
    if il > ir or pl > pr:
        return

    p = preorder[pl]

    postorder(il, idx[p]-1, pl+1, pl+(idx[p]-il))
    postorder(idx[p]+1, ir, pl+(idx[p]-il)+1, pr)

    print(p, end=' ')

    return


for _ in range(int(input())):
    N = int(input())

    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    idx = [-1]*(N+1)
    for i in range(N):
        idx[inorder[i]] = i

    postorder(0, N-1, 0, N-1)
    print()
