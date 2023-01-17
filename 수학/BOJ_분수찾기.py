from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def get_sequence(a:int)->int:
    i=sum=0
    while a>sum:
        sum += i
        i+=1
    return (i-1,sum)

n=int(input())
m,s=get_sequence(n)

if m%2==0: # 짝수면
    node = [1,m]
    for i in range(n-(s-m)-1):
        node[0]+=1
        node[1]-=1
    pass
else: # 홀수면
    node = [m,1]
    for i in range(n-(s-m)-1):
        node[0]-=1
        node[1]+=1

write(str(node[0])+"/"+str(node[1]))