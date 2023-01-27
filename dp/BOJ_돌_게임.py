# https://www.acmicpc.net/problem/9655
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
d=[0]*1_005 # 돌 i개의 게임을 끝내는데 최소한의 게임수
d[1]=1
d[2]=2
d[3]=1

for i in range(4,N+1):
    d[i]=min(d[i-3],d[i-1])+1

if d[N]%2: 
    print("SK")
else: 
    print("CY")