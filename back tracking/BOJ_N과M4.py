# https://www.acmicpc.net/problem/15652
from typing import List
from sys import stdin,stdout
input = stdin.readline
write = stdout.write

"""
중복 가능 수열을 구하는 문제
같은 수를 여러번 골라도 된다.
수열은 비내림차순이여야 한다. i-1번째수은 i번째 수보다 작거나 같아야 한다.

nPm 순열
재귀로 dfs 탐색
같은 수를 여러번 고를수있기에 제약이 없다.
비내림차순으로 순회해야 하기 때문에 순회 조건에 추가해준다.

time: O(n!) n=[1,8]
space: O(n)

print() -> write()로 전환 시 2100ms -> 1264ms 시간을 절약함
"""

def dfs(discovered:List)->None:
    if len(discovered)==m:
        write(str(' '.join(map(str,discovered)))+"\n")
        return
    
    for i in range(1,n+1):
        if ((discovered==[]) or (discovered[-1] <= i)):
            discovered.append(i)
            dfs(discovered)
            discovered.pop()
        
n,m = map(int,input().split())
dfs([])