from sys import stdin,stdout
input,write=stdin.readline,stdout.write

length = 500_000
prime=[True] * length
prime[0]=prime[1]=False
i=2
while i*i<=length:
    if not prime[i]: 
        i+=1
        continue
    for j in range(i*i,length,i):
        prime[j]=False
    i+=1

while True:
    n=int(input())
    if n==0:
        break

    count=0
    for a in range(n+1,2*n+1):
        if prime[a]: count+=1

    write(str(count)+"\n")