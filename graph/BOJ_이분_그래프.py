# https://www.acmicpc.net/problem/1707
from sys import stdin,stdout
from collections import defaultdict,deque
input,write=stdin.readline,stdout.write


"""
인접한 정점은 서로 다른 집합에 속해야함을 이용함
BFS
"""
def solve()->bool:
    group = [-1] * (V+1)
    for i in range(1,V+1):
        if group[i]!=-1: continue
        q = deque([i])
        group[i] = 0
        while q:
            u = q.popleft()
            for v in graph[u]:
                if group[v]!=-1:
                    if group[v]==group[u]: return False
                    else: continue
                group[v]= (group[u]+1)%2
                q.append(v)
    return True

K=int(input())
while K:
    K-=1
    V,E=map(int,input().split())
    graph=defaultdict(list)
    for _ in range(E):
        u,v=map(int,input().strip().split())
        graph[u].append(v)
        graph[v].append(u)
    
    if solve(): write("YES"+"\n")
    else: write("NO"+"\n")
    