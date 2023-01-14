# 연산자 끼워넣기 https://www.acmicpc.net/problem/14888
from sys import stdin,stdout,maxsize
input = stdin.readline
write = stdout.write

"""풀이

숫자 위치는 고정되어 있다.
숫자 사이에 들어가는 연산자만 순서를 바꿀수 있는 연산자에 대한 순열 문제이다.
연산자마다 사용할 수 있는 개수가 정해져있다.
4칙연산 규칙이 없다. 그냥 앞에서 부터 계산하면 된다.
개수를 체크하여 순열을 구하면 된다.

time : O(n!) n=[2,11] 10^7
space : O(n) n=[2,11] 
"""

def recursive(level:int,total:int)->None:
    global mx,mn,count
    
    # 사칙연산 중첩함수
    def calculate(total:int,number:int,op_type:int)->int:
        if op_type==0:
            return total + number
        elif op_type==1:
            return total - number
        elif op_type==2:
            return total * number
        else:
            return int(total / number)

    # 종료
    if level >= n:
        mx,mn= max(mx,total),min(mn,total) # 최댓값,최솟값 업데이트
        return 
    
    # 재귀 
    for op_type in range(4):
        if operators[op_type]>0:
            operators[op_type]-=1 # 방문 체크 표시
            recursive(level+1,calculate(total,numbers[level],op_type)) # 재귀
            operators[op_type]+=1 # 방문 체크 해제

# input
n = int(input())
numbers = list(map(int,input().split()))
operators = list(map(int,input().split()))

# 초기화
mx,mn = -maxsize,maxsize

# 재귀
recursive(1,numbers[0])

# 출력
write(str(mx) + "\n" + str(mn))