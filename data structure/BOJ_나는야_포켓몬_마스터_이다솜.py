# https://www.acmicpc.net/problem/1620
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,M=map(int,input().split())
number_map,string_map={},{}
for i in range(1,N+1):
    s=input().strip()
    number_map[i]=s
    string_map[s]=i
    
for i in range(M):
    s=input().strip()
    if s.isdigit():
        print(number_map[int(s)])
    else:
        print(string_map[s])