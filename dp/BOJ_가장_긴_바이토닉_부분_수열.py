# https://www.acmicpc.net/problem/11054
from sys import stdin, stdout
input, write = stdin.readline, stdout.write

N = int(input())
A = [0]+list(map(int, input().strip().split()))
di = [1]*1_010
dd = [1]*1_010

for i in range(1, N+1):
    for j in range(1, i):
        if A[i] > A[j]:
            di[i] = max(di[i], di[j]+1)

for i in range(N, 0, -1):
    for j in range(N, i, -1):
        if A[i] > A[j]:
            dd[i] = max(dd[i], dd[j]+1)

mx = float('-inf')
for i in range(1, N+1):
    mx = max(mx, dd[i]+di[i]-1)

print(mx)
