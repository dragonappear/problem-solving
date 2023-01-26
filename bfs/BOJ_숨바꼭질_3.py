# https://www.acmicpc.net/problem/13549
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def teleport(num:int):
    tmp=num
    if not tmp: return
    while tmp<=LIMIT and not dist[K]:
        if not dist[tmp]:
            dist[tmp]=dist[num]
            q.append(tmp)
            if tmp==K: return
        tmp <<= 1

N,K=map(int,input().split())
if N==K:
    print(0)
    exit()
    
LIMIT=100_001
dist=[ 0 for _ in range(LIMIT+2)]
q=deque([N])
dist[N]=1
teleport(N)

while not dist[K]:
    u=q.popleft()    
    for n in [u-1,u+1]:
        if not(0<=n<LIMIT) or dist[n]: continue
        dist[n]=dist[u]+1
        q.append(n)
        teleport(n)

print(dist[K]-1)


# teleport 함수를 이용해 현재 보고 있는 u / n의 2의 거듭제곱을 한 번에 처리하는 방식으로 풀이한 코드
