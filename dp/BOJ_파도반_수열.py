# https://www.acmicpc.net/problem/9461
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

d=[0]*(102)
d[0],d[1],d[2],d[3],d[4],d[5],d[6]=1,1,1,2,2,3,4

for i in range(7,102):
    d[i]=d[i-1]+d[i-5]

for _ in range(int(input())):
    N=int(input())
    print(d[N-1])