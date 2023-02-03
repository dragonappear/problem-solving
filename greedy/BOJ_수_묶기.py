# https://www.acmicpc.net/problem/1744
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N=int(input())
A=[int(input()) for _ in range(N)]
pos,neg=[],[] # 양수를 저장하는 리스트, 음수를 저장하는 리스트

ans=0
for n in A:
    if n>1:
        pos.append(n)
    elif n==1: # 1은 어디에나 더하는게 이득
        ans+=1    
    elif n<=0:
        neg.append(n)
        
pos.sort(reverse=True)
neg.sort()

len_p,len_n=len(pos),len(neg)
i=0

for i in range(0,len_p-1,2):
    ans+= (pos[i]*pos[i+1])

if len_p%2==1:
    ans+=pos[-1]

for i in range(0,len_n-1,2):
    ans+= (neg[i]*neg[i+1])
    
if len_n%2==1:
    ans+=neg[-1]

print(ans)
"""
규칙

0,양=>덧셈
0,음=>곱셈

1,양=>덧셈
1,음=>덧셈

양,양->곱셈
양,음->덧셈
음,음->곱셈

양수 리스트는 내림차순 정렬
음수 리스트는 오름차순 정렬

해당 리스트의 길이가 짝수이면 리스트의 숫자를 2개씩 묶어 곱해준다
홀수이면 마지막 숫자를 제외하고 2개씩 곱해주고 마지막 수를 더해준다.

1 인 경우 곱셈을 하면 최댓값이 안나오기 때문에 값에 그냥 1을 더해준다.

"""