# https://www.acmicpc.net/problem/2467
from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
lt, rt = 0, N-1
ans1 = ans2 = float('inf')
while lt < rt:
    if abs(ans1+ans2) > abs(arr[lt]+arr[rt]):
        ans1, ans2 = arr[lt], arr[rt]

    if abs(arr[lt]+arr[rt-1]) <= abs(arr[lt+1]+arr[rt]):
        rt -= 1
    else:
        lt += 1

print(ans1, ans2)
