# https://www.acmicpc.net/problem/1992
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def check(r,c,n):
    for i in range(r,r+n):
        for j in range(c,c+n):
            if graph[i][j]!=graph[r][c]: return False
    return True

def recursive(r,c,n):
    if check(r,c,n):
        return str(graph[r][c])
    
    n = n // 2
    result="("
    result+=recursive(r,c,n)
    result+=recursive(r,c+n,n)
    result+=recursive(r+n,c,n)
    result+=recursive(r+n,c+n,n)
    result+=")"
    
    return result


n=int(input())
graph=[list(map(int,input().strip())) for _ in range(n)]
write(recursive(0,0,n)+"\n")
