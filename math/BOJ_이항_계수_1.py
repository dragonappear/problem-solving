from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def factorial(a:int):
    r = 1
    for i in range(2,a+1):
        r *= i
    return r


n,k=map(int,input().split())
if k<0: write(str(0+"\n"))
elif k>n: write(str(0+"\n"))
else:
    write(str(int((factorial(n)/ (factorial(k)*factorial(n-k)))))+"\n")

