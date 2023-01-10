# https://www.acmicpc.net/problem/15651
from typing import List
import sys
input = sys.stdin.readline

def dfs(discovered:List)->None:
    
    if len(discovered)==m:
        print(*discovered)
        return

    for i in range(1,n+1):
        discovered.append(i)
        dfs(discovered)
        discovered.pop()

if __name__ == "__main__":
    n,m = map(int,input().split())
    dfs([])