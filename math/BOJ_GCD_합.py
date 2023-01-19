from sys import stdin,stdout
from itertools import combinations
input,write=stdin.readline,stdout.write

def gcd(a:int,b:int)->int:
    if a==0: return b
    else: 
        if a<b: a,b=b,a
        return gcd(a%b,b)

for _ in range(int(input())):
    n,*a = map(int,input().split())
    sum = 0
    for x,y in list(combinations(a,2)):
        sum += gcd(x,y)
    write(str(sum)+"\n")