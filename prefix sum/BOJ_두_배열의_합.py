# https://www.acmicpc.net/problem/2143
from sys import stdin
from collections import defaultdict
input = stdin.readline
INF = float('inf')

T = int(input())
n = int(input())
arr1 = [0]+list(map(int, input().split()))

m = int(input())
arr2 = [0]+list(map(int, input().split()))

d1 = [[INF] * (n+1) for _ in range(n+1)]
d2 = [[INF] * (m+1) for _ in range(m+1)]

for i in range(1, n+1):
    arr1[i] += arr1[i-1]

for i in range(1, m+1):
    arr2[i] += arr2[i-1]

for i in range(1, n+1):
    for j in range(1, i+1):
        d1[i][j] = arr1[i]-arr1[j-1]

dic = defaultdict(int)
for i in range(1, m+1):
    for j in range(1, i+1):
        d2[i][j] = arr2[i]-arr2[j-1]
        dic[d2[i][j]] += 1

ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if d1[i][j] == INF:
            continue

        if dic[T-d1[i][j]]:
            ans += dic[T-d1[i][j]]
print(ans)
