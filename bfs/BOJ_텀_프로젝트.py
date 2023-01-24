# https://www.acmicpc.net/problem/9466
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def run(x:int):
    cur=x
    while True:
        state[cur]=x
        cur=A[cur]
        # 이번 방문에서 지나간 학생에 도달했을 경우 -> 싸이클 표시
        if(state[cur]==x):
            while(state[cur]!=-1):
                state[cur]=-1
                cur=A[cur]
            return
        elif state[cur]!=0:
            return
       
for _ in range(int(input())):
    
    N=int(input())
    A = [0] + list(map(int,input().strip().split()))
    # 팀 형성 체크
    # 0 : not visited
    # -1 : cycle_in
    state = [0] * (N+1)
    
    for i in range(1,N+1):
        if state[i]==0: # 방문하지 않은 경우
            run(i)
    
    cnt=0
    for i in range(1,N+1):
        if state[i]!=-1: # 싸이클이 없는 경우
            cnt+=1
            
    print(cnt)