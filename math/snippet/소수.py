# 소수판정 O(lgn)
def isprime(n):
    if n==1: return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

# 에르토스테네스의 체 (O(nlglgn))
N=int(input())
prime = [True] * 1_000_001
prime[1] = False
i=2
while i*i<=N:
    if prime[i]==False: 
        i+=1
        continue
    j = i*i
    while j<=N:
        prime[j]=False
        j+=i
    i+=1

# 소인수 분해 O(lgn)
i = 2
while i*i<=n:
    while(n%i==0):
        n = n//i