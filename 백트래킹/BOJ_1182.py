from sys import stdin,stdout
input = stdin.readline
write = stdout.write

"""
문제:
부분집합을 구해서 하나씩 각각 합을 확인해봐야 하는 문제
DFS로 depth 끝까지 찾은 후 백트래킹 
"""
# time: O(2^n) n[1,20]
# space: O(n)
n,target = map(int,input().split())
arr = list(map(int,input().split()))
visited = [False]*n
count = 0

def dfs(sum:int,depth:int):
    global count

    if depth==n:
        if target==sum:
            count+=1
        return
        
    dfs(sum+arr[depth],depth+1)
    dfs(sum,depth+1)

# 입력값 예외처리
if abs(sum(arr))>1_000_000:
    write(str(0))
else:
    dfs(0,0)
    if target==0: write(str(count-1))
    else: write(str(count))