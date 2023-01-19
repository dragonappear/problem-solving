from sys import stdin,stdout
input,write=stdin.readline,stdout.write


"""

N^N에서 종이의 개수는 9개의 N개의종이의 합이다

1.함수정의:
def recursive(r:int,c:int)-> 0,1,2 개수 더하기

2.base condition
check 같은수: 더한후 return

3.재귀식
9등분
n^2= arr
"""

# 해당 종이 내부에 같은 숫자로만 채워졌는지 확인하는 함수
def check(x:int,y:int,n:int):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j]!= graph[x][y]:
                return False
    return True
    
def solve(x:int,y:int,z:int):
    if check(x,y,z):
        count[graph[x][y]+1]+=1
        return
    
    n = z // 3
    for i in range(3):
        for j in range(3):
            solve(x+i*n , y+j*n , n)

N=int(input())
graph=[list(map(int,input().strip().split())) for _ in range(N)]
count = [0,0,0]
solve(0,0,N)
for c in count:
    write(str(c)+"\n")