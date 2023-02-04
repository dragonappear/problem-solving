# https://www.acmicpc.net/problem/2170
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]

A.sort() # NlogN

st,en=A[0]
cnt=en-st
for i in range(1,N):
    if A[i][0]<=en:  # 시작점이 전 마지막점보다 앞선다면 중복 발생
        if (A[i][1]-en)>0: # 마지막점이 전 마지막점보다 뒤에 있으면 처리
            cnt+= (A[i][1]-en)
            en=A[i][1]
        else:
            continue
    else: 
        st,en=A[i]
        cnt+=(en-st)

print(cnt)