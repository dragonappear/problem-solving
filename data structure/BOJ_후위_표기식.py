# https://www.acmicpc.net/problem/1918
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

expr=input().strip()

postfix=[]
stack=[]

for c in expr:
    if c not in '+-*/()': # 피연산자면 그대로 출력
        postfix.append(c)
    else:
        if c=='(': # ( 는 스택으로 PUSH
            stack.append(c)
        elif c==')':
            while stack and stack[-1]!='(': # )는 (만날때까지 POP
                top = stack.pop()
                postfix.append(top)
            stack.pop() 
        elif c in '+-*/':
            if not stack: # 스택이 비어있으면 연산자 종류 상관없이 PUSH
                stack.append(c)
            elif c=='+' or c=='-':
                while stack and stack[-1]!='(':
                    top = stack.pop()
                    postfix.append(top)
                stack.append(c)
            else:
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    top = stack.pop()
                    postfix.append(top)
                stack.append(c)
while stack:
    postfix.append(stack.pop())
        
write(''.join(postfix)+"\n")