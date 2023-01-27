# https://www.acmicpc.net/problem/2011
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

d=[0]*(5010)
a=[0]*(5010)
MOD=1000000

S=input().strip()
n=len(S)
for i in range(1,n+1):
    a[i]= ord(S[i-1]) - ord('0')

d[0]=1
for i in range(1,n+1):
    if a[i]>0: d[i]= (d[i]+d[i-1]) % MOD
    x = (a[i-1] * 10) + a[i]
    if 10<=x<=26: d[i] = (d[i]+d[i-2]) % MOD

print(d[n])
    