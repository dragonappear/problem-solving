# https://www.acmicpc.net/problem/15649
from typing import List
import sys
input = sys.stdin.readline

def dfs(discovered:List):

    if len(discovered)==m:
        print(*discovered)
        return

    for i in range(1,n+1):
        if not visited[i]:
            visited[i]=True
            discovered.append(i)
            dfs(discovered)
            discovered.pop()
            visited[i]=False
            
if __name__ == "__main__":
    n,m = map(int,input().split())
    visited = [False] * (n+1)
    dfs([])
    
