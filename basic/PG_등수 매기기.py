# https://school.programmers.co.kr/learn/courses/30/lessons/120882
def solution(score):
    N = len(score)
    avg = [(s[0]+s[1])/2 for s in score]
    rank = [0]*N
    for i in range(N):
        cnt = 1
        for j in range(N):
            if i == j:
                continue
            if avg[i] < avg[j]:
                cnt += 1
        rank[i] = cnt
    return rank
