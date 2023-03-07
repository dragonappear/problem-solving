# https://www.acmicpc.net/problem/11055
from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
d = arr[::]  # 초기값 세팅 제대로

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            d[i] = max(d[i], d[j]+arr[i])

print(max(d))
