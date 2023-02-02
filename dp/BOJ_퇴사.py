# https://www.acmicpc.net/problem/14501
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

d=[0]*20 # i번째날부터 N번째날까지 최대수익의 합
t=[0]*20
p=[0]*20
N=int(input())

for i in range(1,N+1):
    t[i],p[i]=map(int,input().split())

for i in range(N,0,-1):
    if i+t[i]<=N+1: # i번째 일에 상담을 할 수 있는 경우
        d[i]=max(d[i+1],d[i+t[i]]+p[i]) # i번째일에 상담을 했을때와 상담을 하지 않았을때 얻을 수 있는 수익 중 최대 수익을 취함
    else:
        d[i]=d[i+1]
        
print(d[1])