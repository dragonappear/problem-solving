import sys
input = sys.stdin.readline

cards = [i for i in range(0,21)]

for _ in range(10):
    start,end = map(int,input().split())

    left = cards[:start] 
    mid = cards[start:end+1]
    mid.reverse()
    right = cards[end+1:] 

    cards = left + mid + right
    
cards.pop(0)
print(*cards)