# https://www.acmicpc.net/problem/2448
from sys import stdin,stdout
input,write=stdin.readline,stdout.write


def fill_star(x:int,y:int):
    graph[x][y]="*"
    graph[x+1][y-1] = graph[x+1][y+1]="*"
    for i in range(y-2,y+3):
        graph[x+2][i]="*"

def recursive(r,c,n):
    if n==3:
        fill_star(r,c)
        return
    
    nn = n//2
    recursive(r,c,nn)
    recursive(r+nn,c-nn,nn)
    recursive(r+nn,c+nn,nn)
    
N=int(input())
graph = [[" "] * (2*N-1) for _ in range(N)]
recursive(0,N-1,N)
for i in graph:
    write(''.join(i)+"\n")