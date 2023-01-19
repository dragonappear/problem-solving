# https://www.acmicpc.net/problem/2630
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

"""
재귀
n번째는 n//4개의 종이를 합친 결과이다.
- 함수정의: 하얀색,파란색 종이의 개수를 더한다
- 함수인자: 행,열,n
- base condition: 같은색으로 이루어져있을때
- 재귀식:
"""

def check(row:int,col:int,n:int):
    for i in range(row,row+n):
        for j in range(col,col+n):
            if graph[i][j]!=graph[row][col]:
                return False
    return True

def recursive(row:int,col:int,n:int):
    if check(row,col,n):
        count[graph[row][col]]+=1
        return
    
    n = n // 2
    recursive(row,col,n)
    recursive(row+n,col,n)
    recursive(row,col+n,n)
    recursive(row+n,col+n,n)

n=int(input())
graph=[list(map(int,input().strip().split())) for _ in range(n)]
count=[0,0]
recursive(0,0,n)
for c in count:
    write(str(c)+"\n")

