# https://www.acmicpc.net/problem/14003
from sys import stdin
from bisect import bisect_left
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
d = [arr[0]]
pos = [0]*N
for i in range(1, N):
    n = arr[i]
    if n > d[-1]:
        d.append(n)
        pos[i] = len(d)-1
    else:
        idx = bisect_left(d, n)
        d[idx] = n
        pos[i] = idx

print(len(d))
mx = len(d)-1
ret = []
for i in range(N-1, -1, -1):
    if pos[i] == mx:
        ret.append(arr[i])
        mx -= 1
        if mx == -1:
            break

print(*reversed(ret))
