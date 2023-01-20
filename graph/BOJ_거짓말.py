# https://www.acmicpc.net/problem/1043
from sys import stdin,stdout
from collections import defaultdict,deque
input,write=stdin.readline,stdout.write

def bfs():
    q = deque()
    for i in range(1,N+1):
        if truth[i]:
            q.append(i)
        
        while q:
            u = q.popleft()
            for v in graph[u]:
                if truth[v]: continue
                truth[v]=True
                q.append(v)

N,M=map(int,input().split()) # N=사람수,M=파티수
know,*know_arr=map(int,input().split()) # 진실을 아는 사람
truth = [False] * (N+1)
parties=[]

for k in know_arr:
    truth[k]=True
    
graph=defaultdict(list)

for _ in range(M):
    party,*party_arr=map(int,input().split()) # 파티에 참여하는 사람
    parties.append(party_arr)
    for i in range(len(party_arr)-1):
        for j in range(i+1,len(party_arr)):
            graph[party_arr[i]].append(party_arr[j])
            graph[party_arr[j]].append(party_arr[i])
            
bfs()

count = 0
for i in range(M):
    flag=True
    for p in parties[i]:
        if truth[p]:
            flag=False
            break
    if flag: count+=1
    
write(str(count)+"\n")