# https://www.acmicpc.net/problem/14889
from sys import stdin, stdout
from itertools import combinations
input, write = stdin.readline, stdout.write


def solve():
    def get_score(arr):
        return sum(board[a][b] for a in arr for b in arr if a != b)

    teams = list(combinations([i for i in range(N)], N//2))  # 1.팀 선정
    mx_cnt = len(list(teams))//2
    ans = float('inf')
    cnt = 0
    for team_a in teams:
        if cnt >= mx_cnt:
            break

        team_b = set([i for i in range(N)]).difference(team_a)
        diff = abs(get_score(team_a)-get_score(team_b))  # 2.계산
        if diff == 0:
            return 0

        ans = min(ans, diff)
        cnt += 1

    return ans


N = int(input())
board = [list(map(int, input().strip().split())) for _ in range(N)]
print(solve())
