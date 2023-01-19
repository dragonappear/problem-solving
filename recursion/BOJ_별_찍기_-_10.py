# https://www.acmicpc.net/problem/2447
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def star(r:int,c:int,n:int):
    if n==1:
        graph[r][c]="*"
        return

    n = n//3
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            star(r+(n*i),c+(n*j) , n)
            
N=int(input())
graph = [ [" "] * N for _ in range(N)]
star(0,0,N)
for g in graph:
    write(''.join(g)+"\n")