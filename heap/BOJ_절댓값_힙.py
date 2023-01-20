# https://www.acmicpc.net/problem/11286
from heapq import heappush,heappop
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

heap=[]
for _ in range(int(input())):
    n=int(input())
    if n==0:
        if not heap:
            write("0\n")
        else:
            m = heappop(heap)
            write(str(m[0]*m[1])+"\n")
    else:
        if n>0: heappush(heap,(n,1))
        else: heappush(heap,(-n,-1))