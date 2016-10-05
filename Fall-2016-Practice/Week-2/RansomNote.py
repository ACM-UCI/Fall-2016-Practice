import collections

def ransom_note(magazine, ransom):
    magazineDict = collections.Counter(magazine)
    ransomDict = collections.Counter(ransom)
    
    for word in ransomDict:
        if word not in magazineDict or magazineDict[word] < ransomDict[word]:
            return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
