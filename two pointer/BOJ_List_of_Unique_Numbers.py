# https://www.acmicpc.net/problem/13144
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
A=list(map(int,input().split()))
chk=[False]*100_002 # 방문표시
cnt=0
chk[A[0]]=True  
rt=0
for lt in range(N):
    while rt<N-1 and not chk[A[rt+1]]:
        rt+=1
        chk[A[rt]]=True # 방문표시
    
    cnt+=(rt-lt+1)
    chk[A[lt]]=False # 방문미표시

print(cnt)