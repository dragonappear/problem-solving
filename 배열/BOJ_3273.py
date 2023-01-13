from sys import stdin,stdout
from collections import defaultdict
input = stdin.readline
out = stdout.write

n = int(input())
arr = list(map(int,input().split()))
x = int(input())

nums_map = {}
count = 0
for a in arr: 
    nums_map[a] = 1
    b = x-a
    if b!=a and b in nums_map:
        count+=1
print(count)