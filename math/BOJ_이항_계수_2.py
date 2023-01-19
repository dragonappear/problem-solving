from sys import stdin,stdout
input,write=stdin.readline,stdout.write

n,k=map(int,input().split())
mod = 10_007

comb = [[0]*1_001 for _ in range(1_001)]

for i in range(1,1_001):
    comb[i][0] = comb[i][i] = 1
    for j in range(1,i):
        comb[i][j] = (comb[i-1][j] + comb[i-1][j-1]) % mod

write(str(comb[n][k]))