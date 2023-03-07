# https://www.acmicpc.net/problem/11054
from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))

d1 = [1]*(N)
d2 = [1]*(N)

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            d1[i] = max(d1[i], d1[j]+1)

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            d2[i] = max(d2[i], d2[j]+1)

for i in range(N):
    d1[i] += (d2[i]-1)

print(max(d1))
