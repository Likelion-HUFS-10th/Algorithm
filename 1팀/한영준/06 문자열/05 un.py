import collections
import sys

words = list(sys.stdin.readline().split())
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = 0
cnt = ""
anagram = []
code = []

for k in range(len(words)):
    words[k] = words[k].upper()
    for i in range(26):
        num = words[k].count(alpha[i])
        cnt = cnt + str(num)
    anagram.append(cnt)
    cnt = ""

set_ana = list(set(anagram))
for a in range(len(set_ana)):
    for b in range(len(anagram)):
        if set_ana[a] == anagram[b]:
            code[a] =b

print(code)



