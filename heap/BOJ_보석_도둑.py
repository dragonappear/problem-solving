# https://www.acmicpc.net/problem/1202
from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input().strip()) for _ in range(K)]

jewels.sort()
bags.sort()

ans = 0
maxh = []  # 보석 가치 최대 힙
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heappush(maxh, -heappop(jewels)[1])
    if maxh:  # heap에는 현재 가방 무게보다 같거나 작은 보석의 가치들로만 채워져 있음
        ans -= heappop(maxh)

print(ans)


"""
명제: 가장 가격이 높은 보석부터 확인하며 해당 보석을 담을 수 있는 가방 중 최대 무게가 가장 작은 가방을 용해 보석을 담는게 이득이다
귀류법1: 가장 가격이 높은 보석 x을 해당 보석을 담을 수 있는 가방 중 최대 무게가 A보다 큰 갑아 B를 이용해 보석을 담는게 더 이득일 수 있는가?
귀류법2: 가장 가격이 높은 보석x을 해당 보석을 담을 수 있는 가방 중 최대 무게가 가장 작은 A가 존재하는데도 불구하고 가방에 넣지 않는게 더 이득일 수 있는가?
"""
