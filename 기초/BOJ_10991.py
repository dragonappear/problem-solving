n = int(input())

for i in range(1,n+1):
    left = " " * (n-i)
    center = ["*"] * (2*i-1)

    for j in range(len(center)):
        if j%2==1:
            center[j]=" "
    print(left + ''.join(center))
