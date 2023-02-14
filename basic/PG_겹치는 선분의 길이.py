# https://school.programmers.co.kr/learn/courses/30/lessons/120876
def solution(lines):
    pos, neg = [0]*(101), [0]*(100)
    for st, en in lines:
        for i in range(st, en):
            if i < 0:
                neg[i] += 1
            else:
                pos[i] += 1

    return sum(1 for n in neg+pos if n >= 2)
