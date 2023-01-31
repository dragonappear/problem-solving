# https://www.acmicpc.net/problem/6603
from sys import stdin,stdout
from itertools import combinations
input,write=stdin.readline,stdout.write

def dfs(start,arr):
    
    if len(arr)==6:
        print(*arr)
        return
    
    for i in range(start,len(A)):
        dfs(i+1,arr+[A[i]])


while True:
    N,*A=list(map(int,input().split()))
    if N==0: break
    # 풀이1
    # dfs(0,[])
    # 풀이2
    for a in combinations(A,6):
        print(*a)
    print()