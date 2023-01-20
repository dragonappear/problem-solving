# https://www.acmicpc.net/problem/11724
from sys import stdin,stdout
from collections import defaultdict,deque
input,write=stdin.readline,stdout.write


N,M=map(int,input().split())
visited= [False] * (N+1)
graph=defaultdict(list)
for _ in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
count = 0
for i in range(1,N+1):
    if not visited[i]:
        count+=1
        stack=[i]
        while stack:
            u = stack.pop()
            if visited[u]: continue
            visited[u]=True
            for v in graph[u]:
                if not visited[v]:
                    stack.append(v)
write(str(count)+"\n")
            


# N,M=map(int,input().split())
# visited= [False] * (N+1)
# graph=defaultdict(list)
# for _ in range(M):
#     u,v=map(int,input().split())
#     graph[u].append(v)
#     graph[v].append(u)
    
# count = 0
# q = deque()
# for i in range(1,N+1):
#     if not visited[i]:        
#         count+=1
#         q.append(i)
#         visited[i]=True
#         while q:
#             u = q.popleft()
#             for v in graph[u]:
#                 if not visited[v]:
#                     q.append(v)
#                     visited[v]=True
    
# write(str(count)+"\n")
        
    
# def dfs(u):
#     if visited[u]: return
    
#     visited[u]=True
#     for v in graph[u]:
#         if not visited[v]: 
#             dfs(v)

# N,M=map(int,input().split())
# visited= [False] * (N+1)
# graph=defaultdict(list)
# for _ in range(M):
#     u,v=map(int,input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# count = 0
# for k in list(graph.keys()):
#     if visited[k]: 
#         continue
#     dfs(k)
#     count+=1
# write(str(count))
