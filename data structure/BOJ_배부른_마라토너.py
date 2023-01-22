# https://www.acmicpc.net/problem/10546
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
s=set()
for _ in range(2*N-1):
    name = input().strip()
    if name in s:
        s.remove(name)
    else:
        s.add(name)
        
write(s.pop())