# https://www.acmicpc.net/problem/2531
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def get_dist(lt,rt):
    if rt>=lt: return (rt-lt+1)
    else: return (N-lt+rt+1)

N,D,K,C=map(int,input().split())
A=[ int(input()) for _ in range(N)]
chk=[0]*(3_010)
cnt=1 # 초밥 가짓수 
ans=0 # 손님이 먹을수있는 초밥 가짓수의 최댓값
chk[A[0]]=1
rt=0
for lt in range(N):
    while rt<N and get_dist(lt,rt)<K: # 순환 체크
        rt+=1
        if rt==N: rt=0
        if chk[A[rt]]==0: cnt+=1
        chk[A[rt]]+=1
            
    if chk[C]==0: ans=max(ans,cnt+1)
    else: ans=max(ans,cnt)
    
    chk[A[lt]]-=1
    if chk[A[lt]]==0: cnt-=1

print(ans)