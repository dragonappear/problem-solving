# https://www.acmicpc.net/problem/1507
from sys import stdin
input = stdin.readline
INF = float('inf')

N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1, N):
        escape = False
        for k in range(N):
            if k == i or k == j:
                continue

            tmp = d[i][k]+d[k][j]

            if d[i][j] == tmp:
                escape = True
                break
            elif d[i][j] > tmp:
                print(-1)
                exit()

        if not escape:
            ans += d[i][j]

print(ans)


"""
i에서 j를 제외한 다른 정점을 k라고 두고,
i에서 k를 거쳐 j로 가는 거리 d[i][k] + d[k][j]를 didk라고 할때,

문제에 입력으로 주어진 배열은 도시 간 최소거리이기 때문에
didk는 d[i][j]보다 작아서는 안된다

작을 경우 -1 출력하고 종료한다

만약 didk==d[i][j] 인 경우 d[i][j]는  d[i][k] + d[k][j] 로 구성된 길이며,
직접 i와 j와 연결하는 유일한 도로가 아니다.

"""
