# https://www.acmicpc.net/problem/20922
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,K=map(int,input().split())
A=list(map(int,input().split()))
chk=[0]*(100_010) # 수열에서 i 포함 개수
cnt=0 # lt에서 rt까지 같은 정수 K를 포함한 원소의 개수
rt=0
chk[A[0]]=1
ans=0 # 최장 연속 부분 수열의 길이
for lt in range(N):
    while rt<N-1 and chk[A[rt+1]]+1<=K:
        rt+=1
        if rt<N: chk[A[rt]]+=1
    
    ans=max(ans,rt-lt+1)
    chk[A[lt]]-=1

print(ans)