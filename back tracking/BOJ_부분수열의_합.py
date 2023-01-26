# https://www.acmicpc.net/problem/1182
from sys import stdin,stdout
input,write = stdin.readline,stdout.write

def dfs(sum,depth):
    global cnt
    
    if depth==N:
        if sum==S: cnt+=1
        return
    
    dfs(sum+A[depth],depth+1)
    dfs(sum,depth+1)

N,S=map(int,input().split())
A=list(map(int,input().strip().split()))
cnt=0
dfs(0,0)
if S==0: print(cnt-1)
else: print(cnt)