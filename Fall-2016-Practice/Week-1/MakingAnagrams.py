import collections
import string

def number_needed(a, b):
    countsA = collections.defaultdict(int)
    countsB = collections.defaultdict(int)
    
    for ch in a:
        countsA[ch] += 1
    
    for ch in b:
        countsB[ch] += 1
        
    totalDiff = 0
    for i in string.ascii_lowercase:
        totalDiff += abs(countsA[i] - countsB[i])
        
    return totalDiff

a = input().strip()
b = input().strip()

print(number_needed(a, b))
