# https://www.acmicpc.net/problem/21318
from sys import stdin
input = stdin.readline

N = int(input())
arr = [0]+list(map(int, input().split()))

psum = [0]*(N+1)

for i in range(1, N+1):
    if arr[i] >= arr[i-1]:
        psum[i] = psum[i-1]
    else:
        psum[i] = psum[i-1]+1

for _ in range(int(input())):
    a, b = map(int, input().split())

    print(psum[b]-psum[a])
