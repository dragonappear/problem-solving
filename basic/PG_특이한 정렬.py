def solution(numlist, n):
    dist = [abs(n-numlist[i]) for i in range(len(numlist))]
    tmp = list(zip(numlist, dist))
    tmp.sort(key=lambda x: (x[1], -x[0]))
    return [x[0] for x in tmp]
