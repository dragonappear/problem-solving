# https://www.acmicpc.net/problem/15650
from typing import List
from sys import stdin,stdout
input = stdin.readline
write = stdout.write

"""
중복되지 않는 수열을 구하는 문제
수열은 오름차순이여야 한다.

nPm 순열
재귀로 dfs 탐색
- 탐색 시 중복체크를 위해 방문체크 배열 사용
  이미 방문했다면 넘어가고, 방문하지 않았다면 방문 표시 dfs
  방문이 끝난 다음에는 다음 순번을 위해 방문 표시 해제

- 오름차순으로 순회하기 위해 인덱스 사용
  시작 인덱스를 dfs에 넘겨주어서 다음 dfs 순서를 결정

time: O(n!) n=[1,8]
space: O(n)
"""

def dfs(index:int,discovered:List)->None:
    if len(discovered)==m:
        write(str(' '.join(map(str,discovered)))+"\n")
        return

    for i in range(index,n+1):
        if not visited[i]:
            visited[i]=True
            discovered.append(i)
            dfs(i+1,discovered)
            discovered.pop()
            visited[i]=False

n,m = map(int,input().split())
visited = [False] * (n+1)
dfs(1,[])