import sys
input = sys.stdin.readline

N = int(input())
M = list(map(int,input().split()))

y_sum = m_sum =  0

for n in M:
    y_sum += (n//30)*10 + 10
    m_sum += (n//60)*15 + 15

if y_sum>m_sum:
    print("M",m_sum)
elif y_sum<m_sum:
    print("Y",y_sum)
else:
    print("Y M",y_sum)