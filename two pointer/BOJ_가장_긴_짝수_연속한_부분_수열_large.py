# https://www.acmicpc.net/problem/22862
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,K=map(int,input().split())
A=list(map(int,input().split()))

cnt=0 # 현재 보고 있는 lt에서 rt 구간에서 홀수의 개수
rt=0
ans=0
if A[0]%2==1: cnt+=1
for lt in range(N):
    while rt<N-1 and cnt+ A[rt+1]%2 <= K:
        rt+=1
        cnt += A[rt]%2
    ans=max(ans,rt-lt+1-cnt)
    cnt-=A[lt]%2
print(ans)