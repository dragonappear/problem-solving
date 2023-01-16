from sys import stdin,stdout
input,write=stdin.readline,stdout.write

m,n = map(int,input().split())
prime = [True] * (n+1)

prime[1] = False

i=2
while i*i<=n:
    if prime[i]==True:
        j=i*i
        while j<=n:
            prime[j]=False
            j+=i
    i+=1

for i in range(m,n+1):
    if prime[i]==True:
        write(str(i)+"\n")