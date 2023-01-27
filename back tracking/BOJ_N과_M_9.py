# https://www.acmicpc.net/problem/15663
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def dfs(arr):
    if len(arr)==M:
        print(*arr)
        return
    
    tmp=0 # 중복 수열인지 확인 하기 위해 필요한 임시 변수
    for i in range(N):
        if visit[i] or tmp==A[i]: continue # 이전 수열의 마지막 항과 새로운 수열의 마지막 항이 같으면 중복 수열
        visit[i]=True
        tmp=A[i]
        dfs(arr+[A[i]])
        visit[i]=False

N,M=map(int,input().split())
A=list(map(int,input().split()))
visit=[False]*N
A.sort()
dfs([])