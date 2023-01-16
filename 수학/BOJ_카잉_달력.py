from sys import stdin,stdout
input,write=stdin.readline,stdout.write


def gcd(a,b):
    if a==0 : return b
    return gcd(b%a,a)

def lcm(a,b):
    return a / gcd(a,b) * b

def solve(m,n,x,y):
    if x==m: x=0
    if y==n: y=0
    l = int(lcm(m,n))
    for i in range(x,l+1,m):
        if i==0:
            continue
        if i%n==y:
            return i
    return -1

for _ in range(int(input())):
    m,n,x,y=map(int,input().split())
    write(str(solve(m,n,x,y))+"\n")