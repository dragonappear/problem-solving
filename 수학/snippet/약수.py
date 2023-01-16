# 약수
def divide(n):
    answer = []
    i=1 
    while i*i<=n:
        if n%i==0: answer.append(i)
        i+=1
    
    for i in range(len(answer)-1,-1,-1):
        if answer[i]*answer[i]==n:continue
        answer.append(n//answer[i])

    return answer

print(divide(16))
    
# 최대공약수
# 유킬리드 호제법
def gcd(a:int,b:int):
    if a==0: return b
    return gcd(a%b,b)

# 최소공배수
def lcd(a,b):
    return a/gcd(a,b) * b 