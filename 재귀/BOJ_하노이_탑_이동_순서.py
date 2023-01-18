from sys import stdin,stdout
input,write=stdin.readline,stdout.write

"""
1초,256MB => O(N)

1. 문제 읽기
2. 논리적 순서
3. 필요한 자료연산 리스트업
4. 자료형, 시간복잡도, 유리한 자료구조 선택
5. 구현
6. 엣지케이스

n-1개 원반은 1->2로 이동하고, n번째 원반은 1->3 으로 이동한다
즉, n번째 원반은 n-1개의 원반을 사용하므로 재귀적으로 풀이가 가능하다.

1. 함수 정의
def hanoi(n:int,a:int,b:int) : n-1개의 원반은 a->b로 옮기고, n번쨰 원반은 a->c로 옮긴다.
2. Base Condition
n==1: return
3. 재귀식
hanoi(n-1,a,6-a-b)
print()
hanoi(n-1,6-a-b,b)
"""

def hanoi(n:int,a:int,b:int):
    if n==1: 
        write(str(a) + ' ' + str(b) + "\n")
        return

    hanoi(n-1,a,6-a-b)
    write(str(a) + ' ' + str(b) + "\n")
    hanoi(n-1,6-a-b,b)

N=int(input())
count,answer= 0,[]
write(str((1<<N)-1)+"\n")
hanoi(N,1,3)
