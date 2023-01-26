# https://www.acmicpc.net/problem/9663
from sys import stdin,stdout
input,write = stdin.readline,stdout.write


def queen(row):
    global cnt
    
    if row==N:
        cnt+=1
        return 
    
    for col in range(N):
        # 행,/,\ 체크
        if vertical[col] or  diag1[row+col] or diag2[row-col+N-1] : continue
        vertical[col]=diag1[row+col]=diag2[row-col+N-1]=True
        queen(row+1)
        vertical[col]=diag1[row+col]=diag2[row-col+N-1]=False
        
N=int(input())
cnt=0
vertical,diag1,diag2=[False]*(N),[False]*(2*N),[False]*(2*N)
queen(0)
print(cnt)