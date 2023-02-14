# https://www.acmicpc.net/problem/23326
from sys import stdin
from bisect import bisect_left
input = stdin.readline

N, Q = map(int, input().split())
lm = set()
for i, v in enumerate(list(map(int, input().split()))):
    if v:
        lm.add(i)

cur = 0
for _ in range(Q):  # Q
    cmd = input().split()
    if cmd[0] == '1':  # O(1)
        i = int(cmd[1])
        if i-1 in lm:
            lm.remove(i-1)
        else:
            lm.add(i-1)

    elif cmd[0] == '2':  # O(1)
        x = int(cmd[1])
        cur += x
        cur %= N

    elif cmd[0] == '3':
        if not lm:
            print(-1)
        else:
            arr = sorted(lm)  # NlogN
            idx = bisect_left(arr, cur)  # logN
            if idx < len(arr) and arr[idx] >= cur:
                print(arr[idx]-cur)
            elif idx < len(arr) and arr[idx] < cur:
                print(N-cur+arr[idx])
