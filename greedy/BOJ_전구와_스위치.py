# https://www.acmicpc.net/problem/2138
from sys import stdin, stdout, setrecursionlimit
input, write = stdin.readline, stdout.write
setrecursionlimit(10**9)


def check(idx, cnt, arr):
    global mn
    if idx == N:
        if arr == target:
            mn = min(cnt, mn)
        return

    if arr[idx-1] != target[idx-1]:
        check(idx+1, cnt+1, switching(idx, arr))
    else:
        check(idx+1, cnt, arr)


def switching(idx, arr):
    for i in range(idx-1, idx+2):
        if (0 <= i < N):
            arr[i] = (arr[i]+1) % 2
    return arr


mn = float('inf')
N = int(input())
arr1 = list(map(int, input().strip()))
arr2 = arr1[::]
target = list(map(int, input().strip()))

check(1, 0, arr1)  # 첫번째 전구 스위치 사용X
check(1, 1, switching(0, arr2))  # 첫번째 전구 스위치 사용O

print(mn if mn != float('inf') else -1)


"""
스위치의 성격상 순간의 선택이 최적의 선택이 될 수 있다 => 그리디 알고리즘
N-1 위치에 있는 전구의 상태를 확정지으려면 N 위치에 있는 전구의 상태를이용하면 된다 => 순서대로 진행 가능
"""
