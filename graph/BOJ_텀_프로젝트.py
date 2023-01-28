# https://www.acmicpc.net/problem/9466
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def visit(start):
    cur=start
    while True: # 계속 순환
        team[cur]=start # 방문 표시
        cur=A[cur] # 다음노드
        if team[cur]==start: # 순환발견
            while team[cur]!=-1: # 순환체크
                team[cur]=-1
                cur=A[cur]
            return # 순환 표시 끝나면
        elif team[cur]!=0: # 이미 다른 정점에서 방문했을 경우 리턴
            return

for _ in range(int(input())):
    N=int(input())
    A=[0]+list(map(int,input().split()))

    team=[0]*(N+1) # 0:미방문,-1:순환소속,else:순환소속X
    for i in range(1,N+1):
        if team[i]==0: visit(i)
    cnt=0
    for i in range(1,N+1):
        if team[i]!=-1: cnt+=1
    print(cnt)