# https://www.acmicpc.net/problem/2473
from sys import stdin
from bisect import bisect_left
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans1 = ans2 = ans3 = float('inf')
for i in range(N):
    for j in range(i+1, N):
        idx = bisect_left(arr, -arr[i]-arr[j])

        for k in range(-2, 3):
            if not(0 <= idx+k < N) or (idx+k == i or idx+k == j):
                continue
            if abs(ans1+ans2+ans3) > abs(arr[i]+arr[j]+arr[idx+k]):
                ans1, ans2, ans3 = arr[i], arr[j], arr[idx+k]

print(*sorted([ans1, ans2, ans3]))
