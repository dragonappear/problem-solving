# https://www.acmicpc.net/problem/1302
from sys import stdin,stdout
from collections import defaultdict
input,write=stdin.readline,stdout.write

mx = float('-inf')
counter = defaultdict(int)
for _ in range(int(input())):
    word=input().strip()
    counter[word]+=1
    if mx < counter[word]:
        mx = counter[word]
        candidates=[word]
    elif mx == counter[word]:
        candidates.append(word)
        
candidates.sort()
write(candidates[0])