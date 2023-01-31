# https://www.acmicpc.net/problem/14002
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

n = int(input())
data = list(map(int, input().split()))
dp = [1] * (n)

for i in range(1,len(data)):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)

mx=max(dp)
print(mx)
result = []
for i in range(n-1, -1, -1):
    if dp[i] == mx:
        result.append(data[i])
        mx -= 1

print(*reversed(result))