from sys import stdin,stdout
from bisect import bisect_left
from collections import defaultdict
input,write=stdin.readline,stdout.write

"""
<solution 0: set>
time:  O(M) M=[1,10_000]
space: O(N) N=[1,10_000]
"""
N,M=map(int,input().split())
count = 0
s = set([input().strip() for _ in range(N)])
for _ in range(M): # O(M)
    input_str = input().strip()
    if input_str in s: #O(1)
        count+=1
write(str(count))


"""
<solution 1: 이분탐색>
time: O(MlogN) M=[1,10_000] N=[1,10_000]
space: O(N) N=[1,10_000]
"""
N,M=map(int,input().split())
count = 0
arr = [input().strip() for _ in range(N)]
arr.sort() #O(NlogN)
for _ in range(M): # O(M)
    input_str = input().strip()
    result = bisect_left(arr,input_str) # O(logN)
    if 0<=result<len(arr) and arr[result]==input_str:
        count+=1
write(str(count))



"""
<solution 2: 트라이>
time: O(N+M) M=[1,10_000] N=[1,10_000]
space: O(N) N=[1,10_000]
"""
class TrieNode:
    def __init__(self) -> None:
        self.word=False
        self.children=defaultdict(TrieNode)

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self,word:str)->None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word=True
    
    def search(self,word:str)->bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

N,M=map(int,input().split())
count = 0
trie = Trie()

for s in list(input().strip() for _ in range(N)): #O(N)
    trie.insert(s)

for _ in range(M): # O(M)
    if trie.search(input().strip()): # O(1)
        count+=1
write(str(count))