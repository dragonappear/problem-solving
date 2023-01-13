# https://www.acmicpc.net/problem/14889
import sys
from typing import List
from itertools import permutations,combinations
input = sys.stdin.readline

# dfs
# team_a를 생성하면 team_b는 자동으로 결정된다
# team_a를 dfs로 구한뒤 계산 후 최솟값 업데이트
# time: O((n)C(n//2)) n is the number of player [4,20]
# space: O(n^2)
mn = float('inf')
def solution_1():
    def dfs(index:int,team_a:List)->None:
        global mn

        # 종료점
        if len(team_a) == players_count // 2 : # O(n^2)
            team_b = [player for player in players if player not in team_a] # O(n)
            a_sum = b_sum = 0
            for player_x in range(players_count//2-1): # O(n^2)
                for player_y in range(player_x+1,players_count//2):
                    a_sum += ability[team_a[player_x]][team_a[player_y]] + ability[team_a[player_y]][team_a[player_x]]
                    b_sum += ability[team_b[player_x]][team_b[player_y]] + ability[team_b[player_y]][team_b[player_x]]
            
            mn = min(mn,abs(a_sum-b_sum))
            return
        
        # DFS
        for member in range(index,len(players)):
            if (len(team_a) < players_count // 2):
                team_a.append(member)
                dfs(member+1,team_a)
                team_a.pop()

    def combinations(n:int,r:int)->int:
        a = 1
        for i in range(n-r+1,n+1):
            a *= i
        for i in range(1,r+1):
            a /= i
        return int(a)
        
    # 초기화
    n = int(input())
    ability = [ list(map(int,input().split())) for _ in range(n)]
    players = [i for i in range(n)]
    players_count = len(players)
    dfs(0,[])
    print(mn)

solution_1()

# 브루트포스 with itertools
# 두 팀의 능력치 차이의 최솟값을 구하는 문제
# A,B 두 팀으로 일단 나눈다 => 조합
# A 팀 계산 - B 팀 계산 => 최솟값 업데이트
def solution_2():
    def get_team_ability(sequence:List):
        return sum(ability[a][b] for a,b in list(permutations(sequence,2)))
    
    # 초기화
    n = int(input())
    ability = [ list(map(int,input().split())) for _ in range(n)]
    players = [i for i in range(n)]
    mn = float('inf')
    
    # 팀 분할
    # space: O(n!)
    team_combinations = list(combinations(players,n//2)) 
    for index,team_a in enumerate(team_combinations): # time: O(n! * n!)

        if(index>=len(team_combinations)//2):
            break
        
        # team a,team b 분할
        team_b = [player for player in players if player not in team_a]
        
        # team a,b 총합 계산
        a_sum,b_sum = get_team_ability(team_a),get_team_ability(team_b) # O(n!)

        # 최솟값 갱신
        mn = min(mn,abs(a_sum-b_sum))
        if mn == 0:
            break
    
    # 출력
    print(mn)


