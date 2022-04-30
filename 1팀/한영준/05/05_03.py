import sys

num = int(sys.stdin.readline())
hansoo = []

for i in range(1,num+1):
    if i<100:
        hansoo.append(i)
    else:

        if (i//100)-((i//10)%10) == ((i//10)%10) - (i%10):
            hansoo.append(i)

print(len(hansoo))
