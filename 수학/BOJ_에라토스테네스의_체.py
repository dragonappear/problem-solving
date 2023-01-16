from sys import stdin,stdout
input,write=stdin.readline,stdout.write

n,k=map(int,input().split())

check =  [True] * (n+1)
check[1] = False

count=0
for i in range(2,n+1):
    if check[i]==True:
        check[i]=False
        count+=1
        if count ==k:
            write(str(i)+"\n")
            exit()
    for j in range(2*i,n+1,i):
        if check[j]==False:
            continue
        check[j]=False
        count+=1
        if count ==k:
            write(str(j)+"\n")
            exit()