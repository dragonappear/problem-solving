# https://www.acmicpc.net/problem/11722
from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))

d = [1]*N

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            d[i] = max(d[i], d[j]+1)

print(max(d))
