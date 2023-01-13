from sys import stdin,stdout
input = stdin.readline
write = stdout.write

"""
모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사하고
탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치되어 있다. 
하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다.

6, 9, 5, 7, 4
"""

n = int(input())
towers = list(map(int,input().split()))
answer = []
stack = []
for i in range(1,len(towers)+1):
    while stack and towers[stack[-1]-1]<towers[i-1]:
        stack.pop()
    if stack:
        answer.append(stack[-1])
    else:
        answer.append(0)
    stack.append(i)

write(str(' '.join(map(str,answer))))
