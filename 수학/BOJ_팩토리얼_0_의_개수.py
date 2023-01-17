from sys import stdin,stdout
input,write=stdin.readline,stdout.write

def get_two_five(n:int):
    global two_count
    global five_count
    # 소인수 분해 O(lgn)
    i = 2
    while i<=n:
        while(n%i==0):
            if i==2: two_count+=1
            elif i==5: five_count+=1
            n = n//i
        i+=1
            
n = int(input())
two_count=five_count=0
for a in range(2,n+1):
    get_two_five(a)

write(str(min(two_count,five_count)))
