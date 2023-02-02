# https://www.acmicpc.net/problem/13305
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

n = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))

total = dist[0] * cost[0]
prev = cost[0]
for i in range(1,len(dist)):
    prev = min(prev,cost[i])
    total += (dist[i]*prev)
    
print(total)