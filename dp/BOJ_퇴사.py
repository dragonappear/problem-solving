# https://www.acmicpc.net/problem/14501
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

d=[0]*(17) # i번째일에 상담 시작했을때 얻을수있는 최대 수익
T=[0]*(17)
P=[0]*(17)


N=int(input().strip())
for i in range(1,N+1):
    T[i],P[i]=map(int,input().strip().split())

for i in range(N,0,-1):
    # i번째 일에 상담을 할 수 있는 경우
    if i+T[i] <= N+1:
        # i번째일에 상담을 했을때와 상담을 하지 않았을때 얻을 수 있는 수익 중 최대 수익을 취함
        d[i] = max(d[i+T[i]] + P[i],d[i+1])
    else:
        d[i]=d[i+1]

print(d[1])