from sys import stdin,stdout
input = stdin.readline
write = stdout.write


"""
* 입력받은 수를 pop 하기 위해서는 이미 수가 스택에 있어야 한다.

- 입력받은 수가 스택에 들어간적이 없다면 push 해준다.
- 스택에 들어간적이 있다면 자신을 만날때까지 pop 해준다.
* 스택의 Top이 입력받은 수보다 작다면 수는 벌써 pop 되었으므로 fail
"""

stack = []
answer = []
start = 1
for _ in range(int(input().strip())):
    n = int(input().strip())

    if start <= n: # 스택에 수가 PUSH 되어있지 않는 경우
        for i in range(start,n+1):
            stack.append(i)
            answer.append("+")
        stack.pop()
        answer.append("-")
        start = n+1
    else:
        if stack and stack[-1]>=n:
            while stack and stack[-1]>=n:
                stack.pop()
                answer.append("-")
        else:
            write("NO")
            exit()

if stack:
    write("NO")
    exit()

for i in answer:
    write(str(i)+"\n")
