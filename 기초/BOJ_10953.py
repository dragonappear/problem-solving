from sys import stdout
n = int(input())
answer = []
for _ in range(n):
    A,B = map(int,input().split(','))
    answer.append(str(A+B))
for a in answer:
    stdout.write(a+"\n")

