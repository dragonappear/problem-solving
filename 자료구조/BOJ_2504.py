# https://www.acmicpc.net/problem/10799
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

'''
괄호를 이용한 스택 문제
올바르지 않은 괄호면 바로 출력 후 종료
올바른 괄호고 스택에 값이 있으면 temp 값에

time: O()
space: O()
'''

s = input().rstrip()
score_map = { '(':2,'[':3}
sum,num= 0,1
stack = []
for i,c in enumerate(s):
    if c == '(':
        num*=2
        stack.append(c)
    elif c == '[':
        num*=3
        stack.append(c)
    elif c == ')':
        if not stack or stack[-1]!='(':
            write(str(0))
            exit()
        if s[i-1]=='(':
            sum += num
        stack.pop()
        num /= 2
    elif c == ']':
        if not stack or stack[-1]!='[':
            write(str(0))
            exit()
        if s[i-1]=='[':
            sum += num
        stack.pop()
        num /= 3

if stack:
    write(str(0))
else:
    write(str(int(sum)))
    