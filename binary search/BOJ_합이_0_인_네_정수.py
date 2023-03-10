# https://www.acmicpc.net/problem/7453
from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

N = int(input())
A, B, C, D = [0]*N, [0]*N, [0]*N, [0]*N

for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

CD = []
for i in range(N):
    for j in range(N):
        CD.append(C[i]+D[j])

CD.sort()
s = set(CD)
ans = 0
for i in range(N):
    for j in range(N):
        t = A[i]+B[j]
        if -t in s:
            ans += (bisect_right(CD, -t)-bisect_left(CD, -t))

print(ans)
