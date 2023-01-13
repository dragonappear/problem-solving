n = int(input())

for i in range(1,n+1):
    left = right = " " * (n-i)
    center = ["*"]*(2*i-1)
    if i<n:
        for i in range(len(center)):
            if i == 0 or i == len(center)-1:
                continue
            center[i]=" "
    
    print(left+''.join(center))