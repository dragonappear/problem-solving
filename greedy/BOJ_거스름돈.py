# https://www.acmicpc.net/problem/14916
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

# sol1: 그리디
N=int(input())
for f in range((N//5)*5,-1,-5):
    if (N-f)%2==0:
        print((f//5)+(N-f)//2)
        exit()
print(-1)

# sol2: dp
N=int(input())
d=[float('inf')]*(100_010) # d[i]=i원의 거스름돈 동전의 최소 개소
d[2],d[4],d[5]=1,2,1 # 초기값

for i in range(6,N+1):
    if d[i-5]==float('inf') and d[i-2]==float('inf'): continue
    d[i]=min(d[i-5],d[i-2])+1 # 점화식
print(d[N] if d[N]!=float('inf') else -1)
