# https://www.acmicpc.net/problem/21757
from sys import stdin
input = stdin.readline

N = int(input())
arr = [0]+list(map(int, input().split()))
L = [0]*(N+1)
R = [0]*(N+1)

for i in range(1, N+1):
    arr[i] += arr[i-1]

for i in range(1, N+1):
    L[i] = L[i-1]
    if arr[N] == 4 * arr[i]:
        L[i] += 1

for i in range(N-1, 0, -1):
    R[i] = R[i+1]
    if arr[N] * 3 == 4 * arr[i]:
        R[i] += 1

ans = 0
for i in range(2, N-1):
    if arr[N] == arr[i]*2:
        ans += L[i-1] * R[i+1]

print(ans)
