# https://www.acmicpc.net/problem/11053
from sys import stdin
input = stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
d = [0] * (N+1)

for i in range(1, N+1):
    for j in range(i):
        if arr[i] > arr[j]:
            d[i] = max(d[i], d[j]+1)

print(max(d))

"""
1. 테이블 정의:
d[i] : i번째 인덱스의 값을 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이

2. 점화식:
d[i] = max(d[j])+1  (1<=j<i and arr[i]<arr[i])

3. 초기값:
d[i] = 0
"""
