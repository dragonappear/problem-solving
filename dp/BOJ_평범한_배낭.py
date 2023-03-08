# https://www.acmicpc.net/problem/12865
from sys import stdin, stdout
input, write = stdin.readline, stdout.write

# 담지않을것인가,담을것인가 선택을 해야한다.
N, K = map(int, input().split())
W, V = [0]*(N+2), [0]*(N+2)
for i in range(1, N+1):
    W[i], V[i] = map(int, input().split())

# SOL 1. 일차원 배열 풀이
# d[i]
# 무게 i의 최대 가치합
d = [0]*(K+10)
for i in range(1, N+1):
    for j in range(K, 0, -1):  # 각각의 무게에 대해서 물건을 포함하여 계산
        if j-W[i] >= 0:  # 무게 j 이하인 물건인지 체크
            d[j] = max(d[j], d[j-W[i]] + V[i])  # 최대 체크
print(d[K])

# SOL 2. 이차원 배열 풀이
# d[i][j]
# i번째까지의 물건까지
# 배낭의 용량이 j였을때 배낭에 들어간 물건의 가치합의 최댓값
N, K = map(int, input().split())
arr = [[0, 0]]+[list(map(int, input().split())) for _ in range(N)]
d = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):  # 개수
    for j in range(1, K+1):  # 무게
        if arr[i][0] > j:  # 물건을 포함할수없다면 포함X
            d[i][j] = d[i-1][j]
        else:  # 포함할수있다면  max(i번째물건포함X,i번째물건포함O)
            d[i][j] = max(d[i-1][j], (d[i-1][j-arr[i][0]] + arr[i][1]))

print(d[N][K])
