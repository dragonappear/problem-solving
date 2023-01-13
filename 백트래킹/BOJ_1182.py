from sys import stdin,stdout
input = stdin.readline
write = stdout.write

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