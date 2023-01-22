# https://www.acmicpc.net/problem/9375
from sys import stdin,stdout
from collections import defaultdict
input,write=stdin.readline,stdout.write

for _ in range(int(input())):
    items=defaultdict(int)
    for _ in range(int(input())):
        name,category=input().split()
        items[category]+=1
    
    ret=1
    for i in items:
        ret*=(items[i]+1)
    write(str(ret-1)+"\n")