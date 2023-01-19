from sys import stdin,stdout
input,write=stdin.readline,stdout.write

"""
스택에 들어가지 않은 경우에는 넣어줘야 하고,
스택에 들어간 경우에는 빼줘야 하므로
스택에 넣은 표시를 해줘야 한다

time: O(n) n=[1,100_000]
space: O(n) n=[1,100_000]
"""

answer,stack = [],[]
start,flag = 1,True
for _ in range(int(input())):
    n=int(input())
    if start<=n: # 스택에 안들어간 경우
        for i in range(start,n+1):
            stack.append(i)
            answer.append("+")
        start=n+1
        stack.pop() 
        answer.append("-")
    else: # 스택에 들어간 경우
        if not stack or (stack and stack[-1]<n): # 이미 POP된 경우
            flag = False
            break
        elif stack and stack[-1]>=n: # POP되지 않은 경우
            while stack[-1]!=n:
                stack.pop()
                answer.append("-")
            stack.pop()
            answer.append("-")

if flag:
    for a in answer:
        write(a+"\n")
else:
    write("NO\n")
    