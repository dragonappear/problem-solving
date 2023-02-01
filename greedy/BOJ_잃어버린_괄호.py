# https://www.acmicpc.net/problem/1541
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

# 최솟값을 만들려면 최대한 큰 수로 빼주면 된다. 즉 덧셈을 먼저 하고, 뺄셈을 한다.
# 최솟값을 만들기 위해서 - 를 기준으로 괄호를 친다
# 55 - 50 + 40 - 30 + 20 -> 55 - (50 + 40) - (30 + 20)
S=input().split('-')
num=[]
for i in S:
    cnt=0
    arr=i.split('+')
    for j in arr:
        cnt+=int(j)
    num.append(cnt)
n=num[0]
for i in range(1,len(num)):
    n-=num[i]
print(n)