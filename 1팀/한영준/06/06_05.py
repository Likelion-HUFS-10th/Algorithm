import sys
word= sys.stdin.readline()
word = word.upper()
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num1, num2 = 0,0
most = ''
for i in range(26):
    num2 = word.count(alpha[i])

    if num1<num2:
        num1 = num2
        most = alpha[i]
    elif num1 == num2:
        most = '?'

print(most)
