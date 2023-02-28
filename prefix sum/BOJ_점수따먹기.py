# https://www.acmicpc.net/problem/1749
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(1, M+1):
        arr[i][j] = tmp[j-1]
        arr[i][j] += arr[i-1][j]

for i in arr:
    print(i)


ans = float('-inf')
for i in range(1, N+1):
    for j in range(i, N+1):
        sum = 0
        for k in range(1, M+1):
            cur = arr[j][k] - arr[i-1][k]
            sum += cur

            if sum < cur:
                sum = cur

            ans = max(ans, sum)

print(ans)
