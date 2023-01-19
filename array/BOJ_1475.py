from collections import Counter

counter = Counter(list(map(int,list(input()))))
answer = 1

for i in range(0,10):
    if i == 6 or i ==9 : continue
    answer = max(answer,counter[i])

print(max(answer,(counter[6]+counter[9]+1)//2))
