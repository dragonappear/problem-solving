from sys import stdin,stdout
input,write=stdin.readline,stdout.write


def is_prime(a:int)->None:
    if a==1: return False
    r=2
    while r*r<=a:
        if a%r==0:
            return False
        r+=1

    return True

n = int(input())
arr = list(map(int,input().strip().split()))
count = 0

for a in arr:
    if a==1: continue
    if is_prime(a): count += 1

print(count)