# https://www.acmicpc.net/problem/2295
from sys import stdin
input = stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
s = set(arr)

two = set()

for i in range(N):
    for j in range(i, N):
        two.add(arr[i]+arr[j])

mx = -1
for i in range(N-1, -1, -1):
    for j in range(i+1):
        if arr[i]-arr[j] in two:
            print(arr[i])
            exit()
