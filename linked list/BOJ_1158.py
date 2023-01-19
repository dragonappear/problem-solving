from sys import stdin,stdout
from collections import deque
input = stdin.readline
write = stdout.write

n,k = map(int,input().split())
queue = deque([i for i in range(1,n+1)])

result= []
while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

answer="<"
for i,n in enumerate(result):
    answer += str(n)
    if i<len(result)-1:
        answer += ", "
answer+=">"

print(answer)