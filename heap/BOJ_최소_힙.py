# https://www.acmicpc.net/problem/1927
from heapq import heappush,heappop
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

heap=[]
for _ in range(int(input())):
    n=int(input())
    if n: heappush(heap,n)
    else:
        if heap: write(str(heappop(heap))+"\n")
        else: write("0\n")