# https://www.acmicpc.net/problem/16987
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def dfs(start):
    global mx

    if start==N:
        cnt=0
        for i in range(N):
            if s[i]<=0: 
                cnt+=1
        mx=max(mx,cnt)
        return
    
    if s[start]<=0: 
        dfs(start+1) # 손에 든 계란이 깨진 경우
    else:
        flag=False
        for i in range(N):
            if i==start or s[i]<=0: continue # 자기자신 or 이미 깨진 계란
            flag=True
            s[start],s[i]= (s[start]-w[i]),(s[i]-w[start])
            dfs(start+1)
            s[start],s[i]= (s[start]+w[i]),(s[i]+w[start])
        if not flag:
            dfs(N)

mx=0
N=int(input())
s,w = [0]*N,[0]*N
for i in range(N):
    s[i], w[i] = map(int, input().split())
dfs(0)
print(mx)