# https://www.acmicpc.net/problem/9084
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())

    d = [0] * 10001
    d[0] = 1

    for i in range(N):
        for j in range(arr[i], M+1):
            d[j] += d[j-arr[i]]

    print(d[M])
