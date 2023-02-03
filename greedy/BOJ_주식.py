# https://www.acmicpc.net/problem/11501
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

for _ in range(int(input())):
    N=int(input())
    D=list(map(int,input().split()))
    
    max_val=D[-1]
    ans=0
    for i in range(N-1,-1,-1):
        if D[i]>max_val: max_val=D[i]
        ans+=max_val-D[i]
    print(ans)
    

"""
아래와 같은 동작을 생각해볼 수 있다. (단, stock[d]는 d일의 주식 가격)

- stock[d] < stock[d+1]이면, 주식을 산다.
- stock[d] > stock[d+1]이면, 주식을 판다.
- stock[d] == stock[d+1]이면 아무것도 안 한다.

하지만, stock[d] > stock[d+1]이더라도 stock[d] < stock[m] 일 수 있다. (단, d < m)
즉, 주식이 다음날 떨어지더라도, 나중에 오를 수 있기 때문에 바로 팔지 않아도 나중에 수익을 낼 수 있다.

핵심: stock[d] < stock[m]인 m이 존재하면, d일에 주식을 사고 m일에 주식을 판다. (단, d < m)

"""