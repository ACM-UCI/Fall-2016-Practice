#!/bin/python3

import sys


def checkAlternating(s, i, j):
    letter1 = str(chr(i + ord('a')))
    letter2 = str(chr(j + ord('a')))
    prevLetter = ''
    for char in s:
        if char == letter1:
            if prevLetter == letter1:
                return False
            else:
                prevLetter = letter1
        elif char == letter2:
            if prevLetter == letter2:
                return False
            else:
                prevLetter = letter2
                
    return True

s_len = int(input().strip())
s = input().strip()

numChars = 26
stringCounts = [0]*numChars
for letter in s:
    index = ord(letter) - ord('a')
    stringCounts[index] += 1

maxLength = 0
for i in range(numChars):
    for j in range(i):
        if stringCounts[i] > 0 and stringCounts[j] > 0 and abs(stringCounts[i] - stringCounts[j]) <= 1:
            newLength = stringCounts[i] + stringCounts[j]
            if checkAlternating(s, i, j) and maxLength < newLength:
                maxLength = newLength
            
print(maxLength)
