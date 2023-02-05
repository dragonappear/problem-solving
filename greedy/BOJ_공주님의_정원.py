# https://www.acmicpc.net/problem/2457
from sys import stdin, stdout
input, write = stdin.readline, stdout.write

N = int(input())
flowers = []
for i in range(N):
    sm, sd, em, ed = map(int, input().strip().split())
    flowers.append((sm*100+sd, em*100+ed))

flowers.sort()

start = 301  # 현재시간
cnt = 0  # 선택한 꽃의 개수
while start < 1201:
    end = start  # 이번에 추가할 꽃으로 인해 변경된 시간

    for i in range(N):
        if (flowers[i][0] <= start) and (flowers[i][1] > end):
            end = flowers[i][1]

    if end == start:  # 시간 start에서 더 전진이 불가능
        print(0)
        exit()
    cnt += 1
    start = end

print(cnt)

"""
그리디한 관점에서 생각해보면 매번 현재 시점에서 피어있는 꽃 중에서 가장 마지막에 지는 꽃을 선택하면 된다

3.1일부터 11.30일까지는 총 276일의 기간이니 모든 꽃이 하루만에 피었다가 진다 해도 최대 276개의 꽃을 선택해도 된다.
즉, 매번 O(N)으로 꽃을 선택해도 된다. 시간복잡도는 최악의 경우 O(276N)이다.

만약 문제가 3월 1일 to 11월 30일이 아니라 1일에서 1,000,000,000일 사이에서 꽃들을 정해야 하는 문제였다면 
매번 O(N)으로 다음 꽃을 탐색하는 풀이는 최대 O(N^2)으로 시간초과일텐데 이 경우 어떻게 해결하면 좋을지 고민해보는걸 추천한다.
"""
