# Assume same keys in each dict
# Return true if any value in dict1 is smaller than the corresponding value in dict2
def isSmallerDict(dict1, dict2):
    for key in dict1:
        if dict1[key] < dict2[key]:
            return True
    return False

n = int(input())
s = input()

counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for ch in s:
    counts[ch] += 1
    
minCountSub = {}
for ch in counts:
    if counts[ch] > n//4:
        minCountSub[ch] = counts[ch] - n//4
    else:
        minCountSub[ch] = 0

if all([minCountSub[i] == 0 for i in minCountSub]):
    print(0)
else:
    p1 = 0
    p2 = 0
    minLength = n
    currCounts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    while p2 < n:
        if isSmallerDict(currCounts, minCountSub):
            # If our current substring is too small, add one more character at the end
            nextChar = s[p2]
            currCounts[nextChar] += 1
            p2 += 1
        else:
            # Otherwise, save the current length, and remove one character at the beginning
            length = p2 - p1
            if length < minLength:
                minLength = length
            
            firstChar = s[p1]
            currCounts[firstChar] -= 1
            p1 += 1
            
    print(minLength)
