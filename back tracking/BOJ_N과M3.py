# https://www.acmicpc.net/problem/15651
from typing import List
from sys import stdin,stdout
input = stdin.readline
write = stdout.write

"""
중복 가능 수열을 구하는 문제
같은 수를 여러번 골라도 된다.

nPm 순열
재귀로 dfs 탐색
같은 수를 여러번 고를수있기에 제약이 없다.
그냥 값을 추가해주면 된다

time: O(n!) n=[1,7]
space: O(n)

print() -> write()로 전환 시 2100ms -> 1264ms 시간을 절약함
"""

def dfs(discovered:List)->None:
    if len(discovered)==m:
        write(str(' '.join(map(str,discovered)))+"\n")
        return

    for i in range(1,n+1):
        discovered.append(i)
        dfs(discovered)
        discovered.pop()

n,m = map(int,input().split())
dfs([])