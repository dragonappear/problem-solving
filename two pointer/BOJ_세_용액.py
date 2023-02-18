# https://www.acmicpc.net/problem/2473
from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = (a[0], a[1], a[2])
min_diff = abs(sum(ans))

for i in range(n - 2):
    left, right = i + 1, n - 1
    while left < right:
        temp_sum = a[i] + a[left] + a[right]
        temp_diff = abs(temp_sum)
        if temp_diff < min_diff:
            min_diff = temp_diff
            ans = (a[i], a[left], a[right])
        if temp_sum < 0:
            left += 1
        else:
            right -= 1

print(*sorted(ans))
