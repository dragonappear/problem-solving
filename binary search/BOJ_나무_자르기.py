# https://www.acmicpc.net/problem/2805
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
TREE = list(map(int, input().split()))

TREE.sort(reverse=True)

lt, rt = 1, TREE[0]

while lt <= rt:
    mid = (lt+rt)//2

    cut = 0
    for t in TREE:
        if t <= mid:
            break
        cut += (t-mid)

    if cut >= M:
        lt = mid+1
    else:
        rt = mid-1

print(lt-1)
