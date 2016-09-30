def parseString(s):
    # If we have a palindrome, we don't have to change it
    if isPalindrome(s):
        return -1
    
    # Otherwise, find the character that doesn't match
    sRev = s[::-1] # Reverse the string
    length = len(s)
    for i in range(length):
        if s[i] != sRev[i]:
            break
            
    # Remove the character that doesn't match from one of the two possible positions
    s1 = s[:i] + s[i + 1:]
    s2 = sRev[:i] + sRev[i + 1:]
    
    if isPalindrome(s1):
        return i
    elif isPalindrome(s2):
        return length - (i + 1)
            
def isPalindrome(s):
    return (s == s[::-1])
        

n = int(input())

for i in range(n):
    s = input()
    print(parseString(s))
