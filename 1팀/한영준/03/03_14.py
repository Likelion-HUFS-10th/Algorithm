import sys

num = int(sys.stdin.readline())
a = num
i = 0

num = (num%10)*10 + ((num//10)+(num%10))%10
i = i+1

while (a != num):
    num = (num % 10) * 10 + ((num // 10) + (num % 10)) % 10
    i = i + 1

print (i)