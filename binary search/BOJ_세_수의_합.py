# https://www.acmicpc.net/problem/2295
from sys import stdin
from bisect import bisect_left
input = stdin.readline

N = int(input())
arr = list(set([int(input().strip()) for _ in range(N)]))
arr.sort()

two = []
for i in range(len(arr)):  # 두 수의 합을 구함
    for j in range(i, len(arr)):
        two.append(arr[i]+arr[j])
two.sort()

for i in range(N-1, -1, -1):  # two[m] + a[j] = a[l] 임을 확인하는 방법
    for j in range(0, i):
        target = arr[i]-arr[j]
        idx = bisect_left(two, target)
        if 0 <= idx < len(two) and two[idx] == target:
            print(arr[i])
            exit()
