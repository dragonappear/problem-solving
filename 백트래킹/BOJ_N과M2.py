# https://www.acmicpc.net/problem/15650
from typing import List
import sys
input = sys.stdin.readline

def dfs(index:int,discovered:List)->None:
    
    if len(discovered)==m:
        print(*discovered)
        return

    for i in range(index,n+1):
        if not visited[i]:
            visited[i]=True
            discovered.append(i)
            dfs(i+1,discovered)
            discovered.pop()
            visited[i]=False
            
if __name__ == "__main__":
    n,m = map(int,input().split())
    visited = [False] * (n+1)
    dfs(1,[])