import sys
input = sys.stdin.readline

arr = [ int(input()) for _ in range(5)]
print(int(sum(arr)/len(arr)),sorted(arr)[2],sep='\n')