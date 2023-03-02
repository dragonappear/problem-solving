# https://www.acmicpc.net/problem/14002
from sys import stdin
from bisect import bisect_left
input = stdin.readline

N = int(input())
arr = [0]+list(map(int, input().split()))
d = [0]*(N+1)
for i in range(1, N+1):
    for j in range(i):
        if arr[i] > arr[j] and d[i] < d[j]+1:
            d[i] = d[j]+1

mx = max(d)
print(mx)
ret = []
for i in range(N, 0, -1):
    if d[i] == mx:
        ret.append(arr[i])
        mx -= 1

    if mx == 0:
        break

print(*reversed(ret))
