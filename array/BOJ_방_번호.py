# https://www.acmicpc.net/problem/1475
from sys import stdin,stdout
from collections import Counter
input,write=stdin.readline,stdout.write

arr= list(map(int,input().strip()))
numbers = [0]*10
mx = float('-inf')
for n in arr:
    numbers[n]+=1
    if n==6 or n==9: continue
    mx = max(mx,numbers[n])
mx = max(mx,(numbers[6]+numbers[9]+1)//2)

write(str(mx))