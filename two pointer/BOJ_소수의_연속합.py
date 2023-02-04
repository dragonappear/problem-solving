# https://www.acmicpc.net/problem/1644
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def get_primes():
    primes=[True]*(N+10)
    primes[1]=False
    i=2
    while i*i<=N:
        if primes[i]==False: 
            i+=1
            continue
        j = i*i
        while j<=N:
            primes[j]=False
            j+=i
        i+=1
    primes=[i for i in range(2,N+1) if primes[i]==True]
    return primes


N=int(input())
if N==1:
    print(0)
    exit()

primes=get_primes()
M=len(primes)
rt=0
tot=primes[0]
cnt=0
for lt in range(M):
    while rt<M and tot<N:
        rt+=1
        if rt!=M: tot+=primes[rt]
    if rt==M: break
    if tot==N: cnt+=1
    tot-=primes[lt]

print(cnt)