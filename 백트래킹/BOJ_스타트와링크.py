# https://www.acmicpc.net/problem/14889
from sys import stdin,stdout
from typing import List
from itertools import permutations,combinations
input = stdin.readline
write = stdout.write

"""
두 팀의 능력치 차이의 최솟값을 구하는 문제
한 팀이 정해지면 나머지 한 팀은 자동으로 멤버가 정해진다.

한 팀의 합이 나머지 팀의 합에 영향을 주지 않는다.
모든 조합에 대해서 계산을 해봐야한다
조합에 대한 연산처리로 itertools를 사용하자

A,B 두 팀으로 일단 나눈다 => 조합
A 팀 계산 - B 팀 계산 => 최솟값 업데이트

time: O((n//2)!) n=[4,20] max: 10^7
space: O(n!)
"""
    
# 초기화
n = int(input())
ability = [ list(map(int,input().split())) for _ in range(n)]
players = [i for i in range(n)]
mn = float('inf')
    
# 팀 분할
# time: O((n)C(n//2))
team_combinations = list(combinations(players,n//2)) 

# 계산
# time: O((n//2)!)
for index,team_a in enumerate(team_combinations): 
    
    def get_team_ability(sequence:List):
        return sum(ability[a][b] for a,b in list(permutations(sequence,2)))

    # 종료점
    if(index>=len(team_combinations)//2):
        break
        
    # team a,team b 분할
    #O(n)
    team_b = [player for player in players if player not in team_a]
        
    # team a,b 총합 계산
    # O((n//2)!) max: 10^6
    a_sum,b_sum = get_team_ability(team_a),get_team_ability(team_b) 

    # 최솟값 갱신
    mn = min(mn,abs(a_sum-b_sum))

    # 0 이하로는 나올 수 없으므로 종료
    if mn == 0:
        break
    
# 출력
write(str(mn))